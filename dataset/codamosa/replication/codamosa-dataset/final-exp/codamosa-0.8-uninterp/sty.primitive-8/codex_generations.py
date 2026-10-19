

# Generated at 2022-06-14 08:21:05.996720
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class R1(RenderType):
        """Dummy class"""

    class R2(RenderType):
        """Dummy class"""

    f1: Callable = lambda *args, **kwargs: "f1 "  # Dummy renderfunc

    f2: Callable = lambda *args, **kwargs: "f2 "  # Dummy renderfunc

    r: Register = Register()

    # Initializing the register
    r.set_eightbit_call(R1)
    r.set_renderfunc(R1, f1)
    r.set_renderfunc(R2, f2)

    assert r(144) == "f1 "
    assert r(r1=144) == "f1 "

    # Change the renderfunc and call the register-object again
    r.set_renderfunc(R1, f2)


# Generated at 2022-06-14 08:21:11.308649
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class A:
        pass

    class B:
        pass

    a: RenderType = A()
    b: RenderType = B()

    def f1(*args):
        return str(args)

    def f2(*args):
        return str(args)

    r = Register()

    r.set_renderfunc(type(a), f1)
    r.set_renderfunc(type(b), f2)

    assert (r.renderfuncs[type(a)] == f1)
    assert (r.renderfuncs[type(b)] == f2)

# Generated at 2022-06-14 08:21:21.414445
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    from .rendertypes import RgbBg, RgbFg, Sgr

    def renderfunc(
        *args: Union[int, float], rtype: RenderType, value: str, mute: bool
    ) -> str:
        if mute:
            return ""
        else:
            return value

    # We create our own test register:
    reg = Register()

    # We set the renderfunc for our register that converts the rendertype
    # to a value:
    reg.set_renderfunc(RgbBg, renderfunc)
    reg.set_renderfunc(RgbFg, renderfunc)
    reg.set_renderfunc(Sgr, renderfunc)

    # We create a new style attribute for our test register:
    reg.new_style = Style(RgbFg(0, 1, 2), Sgr(1))

# Generated at 2022-06-14 08:21:23.920873
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class SampleRegister(Register):
        pass

    new_register = SampleRegister()
    new_register.test_style = Style(RgbBg(3, 5, 7))

    def dummy_renderfunc(*args, **kwargs):
        return "\x1b[44m"

    new_register.set_renderfunc(RgbBg, dummy_renderfunc)

    assert new_register.test_style == "\x1b[44m"



# Generated at 2022-06-14 08:21:35.120849
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    # Create example register
    class DemoRegister(Register):
        orange = Style(value="\x1b[31m")
        blue = Style(value="\x1b[34m")
        green = Style(value="\x1b[32m")

    d = DemoRegister()

    # Mutate all style-attributes with a new render-function
    d.set_renderfunc(RenderType, lambda x: "\x1b[35m")

    assert d.orange == "\x1b[35m"
    assert d.blue == "\x1b[35m"
    assert d.green == "\x1b[35m"

# Unit tests for method mute and unmute of class Register

# Generated at 2022-06-14 08:21:48.873757
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    # Create a new register
    r = Register()

    # Create a dummy rendertype
    Render1 = RenderType("render1")

    # Define a ANSI-sequence for rendertype Render1
    def f1(code):
        return f"\x1b[38;5;{code}m"

    # Define a color
    r.green = Style(Render1(42))

    # Check that the ANSI-sequence was created correctly (without new renderfunc)
    assert str(r.green) != "\x1b[38;5;42m"

    # Add renderfunc to register and update the color
    r.set_renderfunc(Render1, f1)
    r.green

    # Check that the ANSI-sequence was created correctly (with new renderfunc)

# Generated at 2022-06-14 08:22:01.986507
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class RgbRenderType(RenderType):
        __slots__ = ["args"]

        def __init__(self, *args):
            self.args = args

        def render(self, r: int, g: int, b: int) -> str:
            return "RgbRenderType"

    class EightBitRenderType(RenderType):
        __slots__ = ["args"]

        def __init__(self, *args):
            self.args = args

        def render(self, bg_number: int) -> str:
            return "EightBitRenderType"

    # Create Register-Object with EightBitRenderType and RgbRenderType
    register = Register()
    register.set_renderfunc(EightBitRenderType, lambda x: EightBitRenderType())

# Generated at 2022-06-14 08:22:10.329639
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    # We define a dummy rendertype and a dummy render-func
    class MyRenderType(RenderType):
        pass

    def my_render_func(*args):
        return f"foo{args[0]}"

    # We create an instance of Register
    r = Register()

    # We create a style using the dummy rendertype
    r1 = Style(MyRenderType(42))

    # We set the new render type and function
    r.set_renderfunc(MyRenderType, my_render_func)

    # The style r1 should be updated so that the render type is replaced
    assert str(r1) == "foo42"

# Generated at 2022-06-14 08:22:22.489067
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    # Create an empty register
    r = Register()
    s = Style(r.__name__)

    # Define two functions
    def render_t1(*args: int) -> str:
        return f"\x1b[{args[0]};{args[1]};{args[2]}m"

    def render_t2(*args: int) -> str:
        return f"\x1b[{args[0]};{args[1]};{args[2]}m"
    
    # Set renderfunc for one rendertype
    r.set_renderfunc(str, render_t1)
    assert str(Style(*s)) == "\x1b[0;0;0m"
    
    # Set renderfunc for the same rendertype again
    r.set_renderfunc(str, render_t2)

# Generated at 2022-06-14 08:22:33.656812
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    import pytest

    class HtmlFg(RenderType):
        def ansi_render(self):
            return f"<b>{self.args[0]}</b>"

    class RgbFg(RenderType):
        def ansi_render(self):
            r, g, b = self.args
            return f"\x1b[38;2;{r};{g};{b}m"

    def html_render(r, g, b):
        return '<span style="color: rgb(%s,%s,%s)">' % (r, g, b)  # noqa E741

    fg_register = Register()

    fg_register.set_renderfunc(HtmlFg, lambda r, g, b: html_render(r, g, b))

    fg_

# Generated at 2022-06-14 08:22:43.775227
# Unit test for constructor of class Register
def test_Register():
    """
    Unit test for constructor of class Register.
    """
    assert Register()

    import pytest
    with pytest.raises(TypeError):
        Register(42)

# Generated at 2022-06-14 08:22:48.387740
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    register: Register = Register()
    register.red = "red"
    register.blue = "blue"

    assert register.as_dict() == {"red": "red", "blue": "blue"}



# Generated at 2022-06-14 08:22:55.631340
# Unit test for constructor of class Style
def test_Style():
    style = Style(RgbFg(1, 5, 10), Sgr(1))

    assert style == '\x1b[38;2;1;5;10m\x1b[1m'
    assert isinstance(style, str)
    assert isinstance(style, Style)
    assert style.rules == (RgbFg(1, 5, 10), Sgr(1))


# Generated at 2022-06-14 08:23:06.493681
# Unit test for constructor of class Style
def test_Style():
    class Ef(RenderType):
        pass
    class Sgr(RenderType):
        pass
    attrs = {
        'a': Style(),
        'b': Style(Sgr(1)),
        'c': Style(Sgr(1), Sgr(3)),
        'd': Style(Sgr(1), Sgr(3), Ef(1, 2), Ef(3, 4, 5)),
        'e': Style(Ef(1, 2), Sgr(3), Sgr(1)),
        }
    for name, style in attrs.items():
        assert isinstance(style, Style)
        assert isinstance(style, str)
        assert getattr(style, 'rules', None) is not None
        assert isinstance(style.rules, tuple)

# Unit tests to verify if the methods of class Register work

# Generated at 2022-06-14 08:23:15.938429
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    expected_dict = {
        "red": "\x1b[38;2;255;0;0m",
        "dimgray": "\x1b[38;2;105;105;105m",
        "x": "",
    }

    class TestRegister(Register):
        red = Style(RgbFg(255, 0, 0))
        dimgray = Style(RgbFg(105, 105, 105))
        x = Style()

    assert TestRegister().as_dict() == expected_dict



# Generated at 2022-06-14 08:23:21.973835
# Unit test for constructor of class Register
def test_Register():
    r = Register()

    assert (
        r.renderfuncs == {}
    ), "Error: Register class: constructor: attribute 'renderfuncs' is not a empty dict."

    assert r.is_muted == False, "Error: Register class: constructor: attribute 'is_muted' is True, should be False."

    assert (
        hasattr(r, "eightbit_call")
    ), "Error: Register class: constructor: attribute 'eightbit_call' is missing."

    assert (
        hasattr(r, "rgb_call")
    ), "Error: Register class: constructor: attribute 'rgb_call' is missing."



# Generated at 2022-06-14 08:23:33.534911
# Unit test for method mute of class Register
def test_Register_mute():

    # Valid style
    # Test prerequisits:
    # There must be a module-level data-structure
    # that contains all renderfuncs.
    fg = Register()
    fg.renderfuncs = renderfuncs
    fg.red = Style(BashFg(1), TerminalFg(255, 0, 0))
    assert str(fg.red) == "\x1b[31m\x1b[38;2;255;0;0m"
    # Execution:
    # Call method under test
    fg.mute()
    # Test postconditions:
    # The style 'red' must be converted to a style without ANSI-escape-seq
    assert str(fg.red) == ""
    # And method 'is_muted' must return True.
    assert fg.is_m

# Generated at 2022-06-14 08:23:45.384976
# Unit test for method __call__ of class Register
def test_Register___call__():
    # Check if str-call works.
    fg = Register()
    fg.blau = Style(RgbFg(10, 20, 30))
    assert fg("blau") == "\x1b[38;2;10;20;30m"

    # Check if int-call works with rgb.
    fg.rgb = 8
    assert fg(1, 2, 3) == "\x1b[38;2;1;2;3m"

    # Check if int-call works with 8bit.
    fg.eightbit = 16
    assert fg(50) == "\x1b[38;5;50m"

    # Check if wrong type of input raises error.
    # TODO: Do we need this?
    # with pytest.raises(ValueError):
    #     fg("

# Generated at 2022-06-14 08:23:50.799523
# Unit test for method __new__ of class Style
def test_Style___new__():
    s1 = Style(1, 2, 3)
    assert isinstance(s1, Style)
    assert str(s1) == ""

    s2 = Style(1, 2, 3, value="test")
    assert isinstance(s2, Style)
    assert str(s2) == "test"


# Generated at 2022-06-14 08:24:01.094740
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    from .backends.ansi import Style as AnsiStyle, RgbFg
    from .backends.sixel import Style as SixelStyle, RgbFg as SixelRgbFg

    def test_func():

        ansi = Register()
        setattr(ansi, "rgb", AnsiStyle(RgbFg(1, 2, 3)))

        assert "rgb" in dir(ansi)
        assert isinstance(ansi.rgb, Style)
        assert isinstance(ansi.rgb, str)
        assert ansi.rgb == "\x1b[38;2;1;2;3m"

        sixel = Regis

# Generated at 2022-06-14 08:24:08.873277
# Unit test for constructor of class Style
def test_Style():
    assert issubclass(Style, str)


# Generated at 2022-06-14 08:24:20.379500
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    # Initialize a color register with example styles.
    register = Register()

    register.red = Style(RenderType.rgb, RenderType.sgr)
    register.blue = Style(RenderType.rgb, RenderType.sgr)

    # Create a named tuple from the color register.
    namedtuple_register = register.as_namedtuple()

    assert hasattr(namedtuple_register, "blue")
    assert hasattr(namedtuple_register, "red")
    assert not hasattr(namedtuple_register, "yellow")

    assert isinstance(namedtuple_register.blue, str)
    assert isinstance(namedtuple_register.red, str)



# Generated at 2022-06-14 08:24:33.361713
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    # Create a register object
    register_obj = Register()

    # Set the render-function for RgbFg to the method lambda x: f"\x1b[38;2;{x[0]};{x[1]};{x[2]}m"
    register_obj.set_renderfunc(RgbFg, lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m")

    # Set the render-function for Sgr to the method lambda x: f"\x1b[{x}m"
    register_obj.set_renderfunc(Sgr, lambda x: f"\x1b[{x}m")

    # Set the rendertype for RGB-calls to RgbFg

# Generated at 2022-06-14 08:24:39.881390
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .rendertype import RgbFg

    register = Register()
    register.set_renderfunc(RgbFg, lambda r, g, b: "RgbFg({}, {}, {})".format(r, g, b))
    register.set_rgb_call(RgbFg)

    register.red = register(205, 0, 0)

    assert register.red == register(205, 0, 0)

    assert register(205, 0, 0) == "RgbFg(205, 0, 0)"

    assert getattr(register, "red") == "RgbFg(205, 0, 0)"

# Generated at 2022-06-14 08:24:53.410887
# Unit test for method __call__ of class Register
def test_Register___call__():

    class RgbFg(RenderType):
        args = ["r", "g", "b"]

    class RgbBg(RenderType):
        args = ["r", "g", "b"]

    class Bold(RenderType):
        args = []

    class Rgb(RenderType):
        args = ["r", "g", "b"]

    r = Register()

    def render_rgb(r, g, b):
        return f"render_rgb({r}, {g}, {b})"

    def render_eightbit(n):
        return f"render_eightbit({n})"

    r.set_eightbit_call(RgbFg)
    r.set_rgb_call(RgbFg)
    r.set_renderfunc(RgbFg, render_rgb)

# Generated at 2022-06-14 08:25:05.515395
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    # Create a register object.
    from sty import fg, bg
    rg = Register()

    # Create a new renderfunc.
    def func(code: int) -> str:
        # This renderfunc returns a string that is 10 times longer than the given
        # code.
        return str(code)*10

    # Add the new renderfunc to the register and check if new style is rendered
    # properly.
    rg.set_renderfunc(fg, func)
    rg.red = Style(fg.red)
    assert str(rg.red) == "FFFFFFFFFF"

    # Add the old renderfunc to the register and check if old style is rendered
    # properly.
    rg.set_renderfunc(fg, fg._renderfunc)

# Generated at 2022-06-14 08:25:14.804262
# Unit test for method unmute of class Register
def test_Register_unmute():
    class R1(RenderType):
        args = ()
        ansi_code = "1"

    class R2(RenderType):
        args = ()
        ansi_code = "2"

    class R3(RenderType):
        args = ()
        ansi_code = "3"

    def f1():
        return "\x1b[" + R1.ansi_code + "m"

    def f2():
        return "\x1b[" + R2.ansi_code + "m"

    def f3():
        return "\x1b[" + R3.ansi_code + "m"

    reg = Register()

    reg.set_renderfunc(R1, f1)
    reg.set_renderfunc(R2, f2)

# Generated at 2022-06-14 08:25:19.661890
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    register = Register()

    register.test1 = Style(RenderType("test"))
    register.test2 = Style(RenderType("test2"))

    register_tuple = register.as_namedtuple()

    assert hasattr(register_tuple, "test1")
    assert hasattr(register_tuple, "test2")

    assert isinstance(register_tuple, NamedTuple)



# Generated at 2022-06-14 08:25:28.737189
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    register = Register()
    register.set_renderfunc(Type, lambda x: x)

    assert register.rgb_call(0, 0, 0) == (0, 0, 0)

    register.set_rgb_call(Type)
    assert register.rgb_call(1, 2, 3) == (1, 2, 3)

    register.set_rgb_call(None)
    assert str(register.rgb_call(1, 2, 3)) == ""


# Generated at 2022-06-14 08:25:32.900208
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    from .fg import fg
    d = fg.as_dict()
    assert "blue" in d
    assert "red" in d
    assert isinstance(d["blue"], str)
    assert isinstance(d["red"], str)

# Generated at 2022-06-14 08:25:50.707027
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class Sgr(RenderType):
        pass

    def dummy_func(*args, **kwargs):
        return f"{args}{kwargs}"

    register = Register()
    register.set_renderfunc(Sgr, dummy_func)

    assert register.renderfuncs[Sgr] == dummy_func

# Generated at 2022-06-14 08:26:01.468777
# Unit test for method __call__ of class Register
def test_Register___call__():
    rg = Register()

    rg.renderfuncs = {int: lambda x: f"test_{x}", str: lambda x: f"test_{x}"}

    # Test with single int
    rg.set_eightbit_call(int)
    assert rg(123) == "test_123"
    assert rg(255) == "test_255"

    # Test with single str
    rg.set_eightbit_call(str)
    assert rg("test") == "test_test"
    assert rg("123") == "test_123"

    # Test with tuple of 3 ints
    rg.set_rgb_call(int)
    assert rg(1, 2, 3) == "test_1"
    assert rg(42, 255, 5) == "test_42"

    # Test with tuple of 3 strs
   

# Generated at 2022-06-14 08:26:13.186920
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():

    class TestRegister(Register):
        def __init__(self):
            super().__init__()
            self.red = Style("red rule")
            self.blue = Style("blue rule")
            self.green = Style("green rule")

    tr = TestRegister()

    assert isinstance(tr.as_namedtuple(), NamedTuple)
    assert tr.as_namedtuple().red == "red rule"
    assert tr.as_namedtuple().blue == "blue rule"
    assert tr.as_namedtuple().green == "green rule"

    tr = TestRegister()
    assert tr.as_namedtuple() is not tr.as_namedtuple()

# Generated at 2022-06-14 08:26:15.134663
# Unit test for method copy of class Register
def test_Register_copy():

    r = Register()
    b = r.copy()

    return r == b

# Generated at 2022-06-14 08:26:26.452577
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class Null(RenderType):
        @classmethod
        def render(cls, *args, **kwargs):
            return ""

    class StyleR(NamedTuple):
        fg: str
        bg: str
        attr: str

    def render_custom(value: int, *args, **kwargs) -> str:
        return f"{value}"

    r = Register()

    r.set_renderfunc(Null, render_custom)

    assert str(r.yellow) == "1"

    assert r.as_namedtuple() == StyleR(fg="1", bg="2", attr="3")



# Generated at 2022-06-14 08:26:31.310317
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    fg = Register()
    fg.test1 = "test1"
    fg.test2 = "test2"
    assert fg.as_dict() == {"test1": "test1", "test2": "test2"}


# Generated at 2022-06-14 08:26:37.157994
# Unit test for constructor of class Style
def test_Style():
    style1 = Style(RgbFg(10, 42, 144))
    style2 = Style(RgbFg(10, 42, 144), Sgr(1))

    assert isinstance(style1, Style)
    assert isinstance(style2, Style)

    assert isinstance(style1, str)
    assert isinstance(style2, str)

    assert str(style1) == "\x1b[38;2;10;42;144m"
    assert str(style2) == "\x1b[38;2;10;42;144m\x1b[1m"



# Generated at 2022-06-14 08:26:40.392908
# Unit test for constructor of class Register
def test_Register():
    fg = Register()
    assert isinstance(fg, Register)

# Generated at 2022-06-14 08:26:51.594016
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():

    from .sty import fg, bg, ef, ib, rs

    fg('blue')
    StyleRegister = fg.as_namedtuple()
    assert isinstance(StyleRegister, tuple)
    assert isinstance(StyleRegister, NamedTuple)
    assert hasattr(StyleRegister, 'blue')
    assert StyleRegister.blue is not None

    bg('pink')
    StyleRegister = bg.as_namedtuple()
    assert isinstance(StyleRegister, tuple)
    assert isinstance(StyleRegister, NamedTuple)
    assert hasattr(StyleRegister, 'pink')
    assert StyleRegister.pink is not None

    ef('underlined')
    StyleRegister = ef.as_namedtuple()
    assert isinstance(StyleRegister, tuple)

# Generated at 2022-06-14 08:27:00.709958
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    r = Register()
    r.name = Style(RgbFg(1, 5, 10), Sgr(1))
    r.jah = Style(RgbFg(42, 42, 42), Sgr(2, 1))

    assert r.as_dict() == {'name': '\x1b[38;2;1;5;10m\x1b[1m',
                           'jah': '\x1b[38;2;42;42;42m\x1b[2;1m\x1b[0m'}

# Generated at 2022-06-14 08:27:13.636711
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    def test_Sgr(x: int) -> str:
        return "\x1b[0;{}m".format(x)

    r1 = Register()
    r1.set_renderfunc(Sgr, test_Sgr)

    assert test_Sgr(3) == r1(3)

    r1.set_eightbit_call(Sgr)

    assert test_Sgr(3) == r1(3)



# Generated at 2022-06-14 08:27:23.204552
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    class myRgb(namedtuple("myRgb", "r, g, b")):
        __slots__ = ()

    class myEi(namedtuple("myEi", "code")):
        __slots__ = ()

    def myRgbFg(r: int, g: int, b: int) -> str:
        return "\x1b[38;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"

    def myRgbBg(r: int, g: int, b: int) -> str:
        return "\x1b[48;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"


# Generated at 2022-06-14 08:27:36.444000
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    from .fg import fg
    from .bg import bg
    from .ef import ef
    from .rs import rs
    from .constants import StyleProp

    assert fg.blue == bg.blue
    assert fg.red != bg.blue
    assert fg.blue != ef.underline
    assert ef.underline == ef.underline
    assert fg.magenta != "magenta"
    assert fg.magenta != fg.magenta + ef.underline

    fg_dict = fg.as_dict()
    assert isinstance(fg_dict, dict)
    assert fg_blue in fg_dict.values()
    assert "blue" in fg_dict.keys()
    assert "yellow" in fg_dict.keys()
    assert "magenta"

# Generated at 2022-06-14 08:27:42.498550
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    """ Test Register.as_namedtuple() """
    from .rendertype import EightBitFg
    from .ansi import ANSI
    fg = Register()
    fg.red = Style(EightBitFg(9))
    fg.orange = Style(EightBitFg(202))

    nt = fg.as_namedtuple()

    assert nt.red == ANSI.EightBitFg[9]
    assert nt.orange == ANSI.EightBitFg[202]


# Generated at 2022-06-14 08:27:54.186895
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class Rgb(RenderType):
        pass

    class RgbFg(RenderType):
        pass

    def render_rgb(x, y, z):
        return f"\x1b[{x};{y};{z}m"

    def render_rgb_fg(x, y, z):
        return f"\x1b[38;2;{x};{y};{z}m"

    reg = Register()
    reg.rgb1 = Style(Rgb(1, 2, 3))
    reg.rgb2 = Style(RgbFg(1, 2, 3))

    # Test if renderfuncs are empty.
    assert len(reg.renderfuncs) == 0

    assert str(reg.rgb1) == ""
    assert str(reg.rgb2) == ""

   

# Generated at 2022-06-14 08:27:59.557773
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    from .sty import Sty

    s = Sty()
    register = s.fg.red
    assert isinstance(register, Register)
    assert isinstance(register.as_dict(), dict)
    assert register.as_dict() == {"red": "\x1b[31m"}

# Generated at 2022-06-14 08:28:03.751660
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():

    class TestRegister(Register):
        pass

    tr = TestRegister()
    tr.blue = Style("blue", "rule")

    test_reg = tr.as_namedtuple()
    assert test_reg.blue == "blue"



# Generated at 2022-06-14 08:28:08.073413
# Unit test for constructor of class Style
def test_Style():
    s = Style(RgbFg(0,0,0))
    assert len(s.rules) == 1
    assert s.value == "\x1b[38;2;0;0;0m"


# Generated at 2022-06-14 08:28:19.726859
# Unit test for method unmute of class Register
def test_Register_unmute():
    """
    Tests the unmute method of the Register class.
    """

    r1: Register = Register()
    r1.test_style = Style(RgbFg(12, 24, 19))

    assert str(r1.test_style) == ""

    r1.unmute()

    assert str(r1.test_style) == "\x1b[38;2;12;24;19m"

    r2: Register = Register()
    r2.test_style2 = Style(RgbFg(12, 24, 19))

    assert str(r2.test_style2) == "\x1b[38;2;12;24;19m"

    r2.mute()

    assert str(r2.test_style2) == ""

    r2.unmute()


# Generated at 2022-06-14 08:28:31.936505
# Unit test for method __call__ of class Register
def test_Register___call__():
    """
    ANSI codes are generated as strings. In order to test them, we
    need to be able to test string comparison.

    We can use the "scientific" method to generate the expected codes:
    1) Print them to a terminal.

    2) Save the output to a file with a command like this:
    `printf '%b' "\x1b[0m\x1b[1m" > test_file`

    3) Read the output from the file with a command like this:
    `xxd -p test_file`

    4) Copy the output and paste it into this test function.
    """
    def func(x, y, z):
        print(x, y, z)
        return f"{x}{y}{z}"

    r = Register()

    # Test register(42)
    r.set_eight

# Generated at 2022-06-14 08:28:44.697292
# Unit test for method copy of class Register
def test_Register_copy():
    r1 = Register()
    r1.red = Style("")
    r2 = r1.copy()

    r2.red = ""
    assert r1.red == ""

# Generated at 2022-06-14 08:28:48.662840
# Unit test for method mute of class Register
def test_Register_mute():

    from .sty import fg, bg

    # Test if fg and bg have been muted
    fg.mute()
    bg.mute()

    assert not fg.red
    assert not bg.red



# Generated at 2022-06-14 08:29:02.261639
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    from sty import fg, bg, ef, rs

    # Set a new style attribute.
    bg.hello_world = Style(bg.red, ef.bold)

    # Check if new attribute was created.
    assert hasattr(bg, "hello_world")

    # Check if attribute is a Style object.
    assert isinstance(bg.hello_world, Style)

    # Check if attribute is a string.
    assert isinstance(bg.hello_world, str)

    # Check if attribute is a str-subclass.
    assert isinstance(bg.hello_world, Style)

    # Check if the style string contains the right ANSI sequence.
    assert bg.hello_world == "\x1b[41m\x1b[1m"

    # Check if style rules are updated.

    # Set a new style

# Generated at 2022-06-14 08:29:07.884654
# Unit test for method copy of class Register
def test_Register_copy():
    from . import fg, bg

    r: Register = fg
    assert r is not fg
    assert r.is_muted == fg.is_muted
    assert r.renderfuncs is not fg.renderfuncs

    r = bg.copy()
    assert r is not bg
    assert r.is_muted == bg.is_muted
    assert r.renderfuncs is not bg.renderfuncs



# Generated at 2022-06-14 08:29:20.667867
# Unit test for method unmute of class Register
def test_Register_unmute():
    class RgbFg(RenderType):
        args = "r", "g", "b"

    def rgb_render(r: int, g: int, b: int) -> str:
        return f'\x1b[38;2;{r};{g};{b}m'

    # Create a custom register.
    test_class = Register()
    test_class.set_eightbit_call(RgbFg)
    test_class.set_renderfunc(RgbFg, rgb_render)
    test_class.red = Style(RgbFg(1, 20, 40))
    test_class.green = Style(RgbFg(20, 40, 1))
    test_class.blue = Style(RgbFg(40, 1, 20))

    test_class.mute()

    #

# Generated at 2022-06-14 08:29:29.665231
# Unit test for constructor of class Style
def test_Style():

    from sty import fg, bg
    from sty import RgbFg, RgbBg, SgrFg, SgrBg, Sgr

    assert isinstance(fg.red, str)
    assert isinstance(bg.red, str)

    assert isinstance(fg.blue, str)
    assert isinstance(bg.blue, str)

    assert isinstance(fg.orange, str)
    assert isinstance(bg.orange, str)

    assert isinstance(fg.orange, Style)
    assert isinstance(fg.orange.rules[0], RgbFg)
    assert isinstance(fg.orange.rules[1], SgrFg)


# Generated at 2022-06-14 08:29:34.943123
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    import sty
    fg = sty.fg
    fg.eightbit_call = lambda x: "hahaha, this is not the same renderfunc anymore."
    assert fg.eightbit_call(42) == "hahaha, this is not the same renderfunc anymore."

# Generated at 2022-06-14 08:29:42.551918
# Unit test for constructor of class Style
def test_Style():
    style = Style(RgbFg(1, 2, 3), RgbBg(4, 5, 6))
    assert isinstance(style, str)
    assert isinstance(style, Style)
    assert style.rules[0]._name == "RgbFg"
    assert style.rules[1]._name == "RgbBg"
    assert style == '\x1b[38;2;1;2;3m\x1b[48;2;4;5;6m'



# Generated at 2022-06-14 08:29:50.899622
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    from sty import fg, RenderType

    class MyRender(RenderType):
        pass

    def my_render_func(x: int) -> str:
        return "MyRender -> " + str(x)

    # Set the render-func for MyRender-type.
    fg.set_renderfunc(MyRender, my_render_func)

    # Create a style using the new render-func.
    fg.my_style = Style(MyRender(42))

    # Call the style using my_render_func.
    assert str(fg.my_style) == "MyRender -> 42"

# Generated at 2022-06-14 08:29:51.641963
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    pass

# Generated at 2022-06-14 08:30:11.312732
# Unit test for method __new__ of class Style
def test_Style___new__():

    from .rendertype import AnsiFG, AnsiBG, Sgr, RenderTypeOne, RenderTypeTwo

    class CustomRegister(Register):
        pass

    # Instantiate register.
    custom_register = CustomRegister()

    # Add a test-rendertype.
    custom_register.set_renderfunc(RenderTypeOne, lambda *args: f"Sgr(*{args})")

    # Create test style from Sgr-object.
    style_1 = Style(RenderTypeOne(1, 2, 3))

    # Check whether style_1 is an instance of String.
    assert isinstance(style_1, str)

    # Check whether style_1 is an instance of Style.
    assert isinstance(style_1, Style)

    # Check whether style_1 is of type str.
    assert type(style_1) == str

    # Check

# Generated at 2022-06-14 08:30:18.829797
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():

    # type: Register
    rg = Register()
    rg.set_renderfunc(RenderType, lambda x: x)
    rg.r = Style(RenderType(42))

    # We do not want to raise a TypeError
    assert rg.as_namedtuple().r == '\x1b[42m'

    tpl = rg.as_namedtuple()
    assert isinstance(tpl, NamedTuple)
    assert tpl.r == '\x1b[42m'



# Generated at 2022-06-14 08:30:28.318227
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    from .sty import Sty

    mysty = Sty()

    # Create a custom render type
    class MyRenderer(RenderType):
        def render(self, *args):
            return "\x1b[31m"
    mysty.add_rendertype(MyRenderer)

    # Add custom register
    mysty.add_register("custom", "red")
    mysty.custom.set_renderfunc(MyRenderer, MyRenderer.render)

    # Compare namedtuple
    assert mysty.custom.as_namedtuple() == mysty.custom.as_dict()

# Generated at 2022-06-14 08:30:38.275378
# Unit test for method mute of class Register
def test_Register_mute():
    from .ansi import ANSI
    from .rendertype import Sgr
    from .sty import fg

    aset: RenderType = ANSI.SGR_SET

    fg.red = Style(Sgr(31))

    fg.mute()

    assert fg.red.value == ""

    assert str(fg.red) == ""

    assert fg(31) == ""

    assert fg(10, 40, 40) == ""

    fg.unmute()

    assert fg.red.value == aset(31)

    assert str(fg.red) == aset(31)

    assert fg(31) == aset(31)

    assert fg(10, 40, 40) == aset(10, 40, 40)

# Generated at 2022-06-14 08:30:50.277244
# Unit test for method unmute of class Register
def test_Register_unmute():
    class TestRegister(Register):
        def __init__(self):
            super().__init__()

            self.foo = Style(RgbFg(1,2,3))
            self.bar = Style(RgbBg(4,5,6), RgbFg(7,8,9))

    register = TestRegister()
    assert not register.is_muted
    assert getattr(register.foo, "value") == "\x1b[38;2;1;2;3m"
    assert getattr(register.bar, "value") == "\x1b[48;2;4;5;6m\x1b[38;2;7;8;9m"

    register.mute()
    assert register.is_muted
    assert getattr(register.foo, "value") == ""
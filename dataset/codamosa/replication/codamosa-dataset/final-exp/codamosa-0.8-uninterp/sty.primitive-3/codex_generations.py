

# Generated at 2022-06-14 08:20:44.774278
# Unit test for method __call__ of class Register
def test_Register___call__():

    class MyRegister(Register):
        def __init__(self):
            super().__init__()
            self.foo = Style(RgbFg(1, 5, 10))

    r: MyRegister = MyRegister()
    assert r.foo == r("foo")
    assert r.foo == r.foo


# Generated at 2022-06-14 08:20:47.859405
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    r.red = Style(r.renderfuncs.RgbFg(100, 120, 140))

# Generated at 2022-06-14 08:20:52.071412
# Unit test for constructor of class Register
def test_Register():
    register = Register()
    assert isinstance(register, Register)
    assert isinstance(register, object)
    assert not hasattr(register, "name")
    register.name = "name"
    assert hasattr(register, "name")



# Generated at 2022-06-14 08:21:00.932273
# Unit test for constructor of class Register
def test_Register():

    # Default
    r1 = Register()
    assert r1.is_muted is False
    assert r1.eightbit_call(1) == ""

    # Tests constructor parameters
    r2 = Register()
    assert r2.is_muted is False
    assert r2.eightbit_call(1) == ""

    # Muted
    r3 = Register()
    r3.is_muted = True
    assert r3.is_muted is True
    assert r3.eightbit_call(1) == ""



# Generated at 2022-06-14 08:21:03.799983
# Unit test for constructor of class Register
def test_Register():

    class TestRegister(Register):
        pass

    r = TestRegister()
    assert isinstance(r, Register)



# Generated at 2022-06-14 08:21:17.069470
# Unit test for method __call__ of class Register
def test_Register___call__():
    import unittest.mock as mock

    # Let's make a mock renderfunc that behaves as if it is used
    # in a register.
    f1 = mock.MagicMock()

    # The mock-function returns the arguments it was called with.
    f1.return_value = lambda *args, **kwargs: (args, kwargs)

    # We test the calls against some dummy register.
    register = Register()

    # Let's set the renderfunc with our mock-renderfunc to the
    # register.
    register.set_eightbit_call(f1)

    # Now let's test the function.

# Generated at 2022-06-14 08:21:20.563116
# Unit test for constructor of class Register
def test_Register():
    register = Register()
    assert register.renderfuncs == {}
    assert register.is_muted is False
    assert register.eightbit_call(0) == 0
    assert register.rgb_call(0, 0, 0) == (0, 0, 0)


# Generated at 2022-06-14 08:21:22.816255
# Unit test for constructor of class Register
def test_Register():
    register = Register()
    assert register.as_dict() == {}, "Register constructor test: failed"



# Generated at 2022-06-14 08:21:30.853575
# Unit test for constructor of class Register
def test_Register():
    renderfuncs_ = {RgbFg: lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m"}
    r = Register()
    r.renderfuncs = renderfuncs_

    # Create new style
    r.mystyle = Style(RgbFg(10, 20, 30), Sgr(1))

    assert r.mystyle == "\x1b[38;2;10;20;30m\x1b[1m"

# Generated at 2022-06-14 08:21:37.004588
# Unit test for method __call__ of class Register
def test_Register___call__():

    class CustomRegister(Register):
        pass

    r = CustomRegister()

    r.set_renderfunc(RenderType, lambda x: f"\x1b[{x}m")
    r.set_eightbit_call(RenderType)

    # Create a simple style attribute
    r.red = Style(42)

    # Simple 8bit call
    assert r(42) == r.red

    # Simple string call
    assert r("red") == r.red

# Generated at 2022-06-14 08:21:47.618852
# Unit test for method __call__ of class Register
def test_Register___call__():
    r = Register()

    r.set_eightbit_call(RenderType)
    r.set_rgb_call(RenderType)

    r.renderfuncs.update({
        RenderType : lambda x: "RENDERED-STRING"
    })

    assert r() == ""
    assert r(42) == "RENDERED-STRING"
    assert r(10, 40, 255) == "RENDERED-STRING"

# Generated at 2022-06-14 08:21:53.769140
# Unit test for method __call__ of class Register
def test_Register___call__():

    class TestRegister(Register):
        black = Style()

    r1 = TestRegister()
    assert r1.black == r1("black")

    packed_rgb = TestRegister()
    packed_rgb.red = Style(RgbFg(1, 2, 3))
    assert packed_rgb.red == packed_rgb(1, 2, 3)

    fg = TestRegister()
    fg.red = Style(Sgr(1))
    assert fg.red == fg(1)

# Generated at 2022-06-14 08:22:05.361066
# Unit test for method __call__ of class Register
def test_Register___call__():

    import pytest

    fg: Register = Register()
    fg.red = Style()

    assert fg("red") == ""

    # Test 8bit call
    fg.set_eightbit_call(RenderType)
    fg.red = Style(RenderType(41))

    assert fg(41) == "\x1b[38;5;41m"

    # Test rgb call
    fg.set_rgb_call(RenderType)
    fg.red = Style(RenderType(255, 0, 0))

    assert fg(255, 0, 0) == "\x1b[38;2;255;0;0m"



# Generated at 2022-06-14 08:22:14.283336
# Unit test for constructor of class Register
def test_Register():

    class MyRenderer(RenderType):
        ANSI_CODE = 123

    def renderfunc(self: RenderType, *args, **kwargs) -> str:
        return f"\x1b[{self.ANSI_CODE}m"

    r = Register()
    r.set_renderfunc(MyRenderer, renderfunc)
    assert r.renderfuncs[MyRenderer] == renderfunc

    r.set_eightbit_call(MyRenderer)
    assert r(100) == "\x1b[123m"

    r.set_rgb_call(MyRenderer)
    assert r(100, 50, 20) == "\x1b[123m"



# Generated at 2022-06-14 08:22:16.038555
# Unit test for constructor of class Register
def test_Register():
    r = Register()

    assert(isinstance(r, Register))

# Generated at 2022-06-14 08:22:25.642174
# Unit test for method __call__ of class Register
def test_Register___call__():

    from .rendertype import RgbFg, Sgr

    r = Register()
    r.renderfuncs.update({Sgr: lambda *x: "S" + str(x), RgbFg: lambda *x: "RF" + str(x)})

    r.black = Style(Sgr(0), RgbFg(1, 2, 3))
    r.black_bold = Style(Sgr(1), r.black)

    assert str(r.black) == "RF(1, 2, 3)S(0)"
    assert r.black == "RF(1, 2, 3)S(0)"
    assert r.black_bold == "RF(1, 2, 3)S(0)S(1)"
    assert r(0) == "S(0)"

# Generated at 2022-06-14 08:22:40.490519
# Unit test for method __call__ of class Register
def test_Register___call__():

    # It should return empty string if muted.
    r = Register()
    assert str(r(42)) == ""

    # It should return attribute if it is a string.
    r = Register()
    r.foo = Style(RenderType.Reset)
    assert str(r("foo")) == str(r.foo)

    # It should return attribute if it is a string.
    r = Register()
    r.foo = Style(RenderType.Reset)
    assert str(r(42)) == ""

    # It should return correct attribute.
    r = Register()
    r.foo = Style(RenderType.Bold)
    r.bar = Style(RenderType.Italic)
    assert str(r("foo")) == str(r.foo)
    assert str(r("bar")) == str(r.bar)

    #

# Generated at 2022-06-14 08:22:42.108566
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert isinstance(r, Register)


# Generated at 2022-06-14 08:22:44.428323
# Unit test for constructor of class Register
def test_Register():
    """
    Unit test for constructor of class Register.
    """
    reg = Register()
    assert isinstance(reg, Register)


# Generated at 2022-06-14 08:22:57.948799
# Unit test for method __call__ of class Register
def test_Register___call__():

    # Test Eightbit-call
    r = Register()
    r.set_eightbit_call(RenderType.Eightbit)
    r.renderfuncs.update({RenderType.Eightbit: lambda x: str(x)})
    assert r(42) == "42"

    # Test String-call
    r.red = Style(RenderType.Eightbit(3))
    assert r("red") == "\x1b[38;5;3m"

    # Test Rgb-call
    r.set_rgb_call(RenderType.RgbFg)
    r.renderfuncs.update({RenderType.RgbFg: lambda r, g, b: (r, g, b)})
    assert r(10, 42, 255) == (10, 42, 255)

# Generated at 2022-06-14 08:23:15.374231
# Unit test for method __call__ of class Register
def test_Register___call__():

    # Test if empty string is returned when called with wrong number of parameters.
    class TestRegister(Register):
        pass

    t = TestRegister()
    assert t("foo", "bar") == ""
    assert t("foo", "bar", "baz") == ""

    # Test if a 'string'-call returns the style that has the same name.
    class TestRegister(Register):
        foo = Style("Sty", value="")

    t = TestRegister()
    assert t("foo") == ""

    # Test if an 'eightbit'-call returns the expected string.
    class TestRegister(Register):
        def render(self, x):
            return "RENDER " + str(x)

    t = TestRegister()

    t.set_renderfunc(str, t.render)

    t.set_eightbit_call(str)

   

# Generated at 2022-06-14 08:23:22.628294
# Unit test for method __call__ of class Register
def test_Register___call__():

    def rf_int(i):
        return f"\x1b[{i}m"

    def rf_rgb(r, g, b):
        return f"\x1b[48;2;{r};{g};{b}m"

    from sty import fg, bg

    fg.set_renderfunc(int, rf_int)
    bg.set_renderfunc(int, rf_rgb)

    fg.set_eightbit_call(int)
    bg.set_rgb_call(int)

    assert fg(11) == "\x1b[11m"
    assert bg(42, 42, 42) == "\x1b[48;2;42;42;42m"
    assert fg.red == "\x1b[31m"

# Generated at 2022-06-14 08:23:26.906355
# Unit test for constructor of class Register
def test_Register():
    """
    Tests that the Register class initializes correctly.
    """
    r = Register()
    assert isinstance(r, Register)
    assert len(r.renderfuncs) == 0
    assert not r.is_muted



# Generated at 2022-06-14 08:23:28.576162
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert isinstance(r, Register)


# Generated at 2022-06-14 08:23:30.248727
# Unit test for constructor of class Register
def test_Register():

    r = Register()
    assert isinstance(r, Register)



# Generated at 2022-06-14 08:23:32.085463
# Unit test for constructor of class Register
def test_Register():
    register = Register()
    assert register.is_muted == False

# Generated at 2022-06-14 08:23:38.287867
# Unit test for constructor of class Register
def test_Register():

    new_register = Register()
    attrs = dir(new_register)
    # Default attributes: set_eightbit_call, set_rgb_call, set_renderfunc, eightbit_call,
    # rgb_call, renderfuncs, is_muted
    assert len(attrs) == 7
    assert new_register.is_muted == False



# Generated at 2022-06-14 08:23:44.222405
# Unit test for constructor of class Register
def test_Register():

    # Create new register with empty renderfuncs dict.
    reg: Register = Register()

    # Test for init (attributes must be initialized correctly)
    assert reg.renderfuncs == {}
    assert reg.is_muted is False
    assert reg.eightbit_call is not None
    assert reg.rgb_call is not None

# Generated at 2022-06-14 08:23:55.078463
# Unit test for method __call__ of class Register
def test_Register___call__():

    import sys

    # TODO: Test if output matches styling.

    # Test calls on empty Register object
    reg_test = Register()
    assert reg_test(1) == ""
    assert reg_test(1, 2, 3) == ""
    assert reg_test("name") == ""
    assert reg_test() == ""
    assert reg_test(1, 2, 3, 4) == ""

    len_ = len(sys.stdout.write.__closure__)  # type: ignore

    # Test calls with different renderfuncs
    reg_test.set_renderfunc(str, sys.stdout.write)
    reg_test.foo = Style(str("foo"))
    assert reg_test(1) == ""
    assert reg_test(1, 2, 3) == ""

# Generated at 2022-06-14 08:24:04.979866
# Unit test for method __call__ of class Register
def test_Register___call__():
    """
    The __call__ method of the Register-class has to handle three different
    types of calls:

        - Int-Call (`fg(42)`)
        - RGB-Call (`fg(10, 42, 255)`)
        - Name-Call (`fg('red')`)

    This unit test makes sure that these call can be done as expected.
    """

    from .rendertype import EightBit, Rgb
    from .register import fg

    # Set up test-register and define render functions for eightbit and rgb.
    register = Register()
    register.set_renderfunc(EightBit, lambda x: f"\x1b[38;5;{x}m")

# Generated at 2022-06-14 08:24:22.824349
# Unit test for method __new__ of class Style
def test_Style___new__():
    rule1 = Sgr(1)  # bold
    rule2 = RgbFg(1, 5, 10)  # orange

    style = Style(rule1, rule2)

    assert str(style) == "\x1b[1m\x1b[38;2;1;5;10m"
    assert style.rules == (rule1, rule2)
    assert isinstance(style, str)
    assert not isinstance(style, Sgr)  # Sgr is a subclass of Style
    assert not isinstance(style, RgbFg)  # RgbFg is a subclass of Style

    assert str(Style(Sgr(2))) == "\x1b[2m"



# Generated at 2022-06-14 08:24:28.531753
# Unit test for method __new__ of class Style
def test_Style___new__():
    assert Style("dummy_rule").value == ""
    assert Style("dummy_rule").rules == ("dummy_rule",)
    assert isinstance(Style("dummy_rule"), Style)
    assert isinstance(Style("dummy_rule"), str)
    assert str(Style("dummy_rule")) == "dummy_rule"



# Generated at 2022-06-14 08:24:36.555263
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    """
    In this test we make sure that the set_renderfunc() method
    works as intended.
    """

    from .rendertype import RgbBg, RgbFg, Sgr

    def dummy_renderfunc(code: int) -> str:
        return "foo" + str(code)

    r = Register()

    r.set_renderfunc(RgbFg, dummy_renderfunc)

    assert r.renderfuncs.get(RgbFg, None) == dummy_renderfunc

    r.red = Style(RgbFg(1, 2, 3), Sgr(1))

    assert str(r.red) == "foofoo1foo2foo3foo1"

    r.set_renderfunc(RgbFg, None)


# Generated at 2022-06-14 08:24:39.598144
# Unit test for method unmute of class Register
def test_Register_unmute():
    r = Register()
    r.is_muted = True
    r.red = Style(RgbFg(255, 0, 0))
    assert r.red == ""

    r.unmute()
    assert r.red == "\x1b[38;2;255;0;0m"

# Generated at 2022-06-14 08:24:53.015433
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    from .typing import SgrFg

    class RgbFg(RenderType):
        """
        This class represents a rgb foreground color.
        """

    # Create renderfuncs dictionary
    renderfuncs = {SgrFg: lambda fg_color: f"\x1b[38;5;{fg_color}m",
                   RgbFg: lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m"}

    # Create Register object
    register = Register()
    register.set_renderfunc(RgbFg, renderfuncs[RgbFg])

    # Create Style object using SgrFg as rendertype
    style = Style(SgrFg(17))

    # Set style as attribute
    setattr(register, "red", style)



# Generated at 2022-06-14 08:25:05.289517
# Unit test for constructor of class Style
def test_Style():

    from sty.rendertype import Sgr, RgbFg, RgbBg, RgbExt

    underline = Style(Sgr(4))
    fg_red = Style(RgbFg(255, 0, 0))
    fg_red_bold = Style(RgbFg(255, 0, 0), Sgr(1))

    assert isinstance(underline, Style)
    assert isinstance(fg_red, Style)
    assert isinstance(fg_red_bold, Style)
    assert str(fg_red) == "\\x1b[38;2;255;0;0m"
    assert str(fg_red_bold) == "\\x1b[38;2;255;0;0m\\x1b[1m"

# Generated at 2022-06-14 08:25:16.344229
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():

    class Tmp(Register):
        deutsch = Style(Reset(), Foreground(1), Sgr(1), Value="\x1b[39m\x1b[1m")
        french = Style(Reset(), Foreground(2), Sgr(1), Value="\x1b[39m\x1b[1m")
        italian = Style(Reset(), Foreground(3), Sgr(1), Value="\x1b[39m\x1b[1m")

    r = Tmp()

    tup = r.as_namedtuple()

    assert isinstance(tup, NamedTuple)
    assert tup.deutsch == "\x1b[39m\x1b[1m"
    assert tup.french == "\x1b[39m\x1b[1m"


# Generated at 2022-06-14 08:25:16.848847
# Unit test for constructor of class Register
def test_Register():
    assert Register()

# Generated at 2022-06-14 08:25:22.284375
# Unit test for method copy of class Register
def test_Register_copy():
    """
    Test the `copy` method of the `Register` class.
    """
    reg1 = Register()

    setattr(reg1, "red", Style("\033[31m"))

    reg2 = reg1.copy()

    assert reg1 is not reg2

    assert getattr(reg1, "red") is not getattr(reg2, "red")

    assert getattr(reg1, "red") == getattr(reg2, "red")



# Generated at 2022-06-14 08:25:28.531301
# Unit test for constructor of class Style
def test_Style():
    s = Style(RgbFg(255, 0, 0), RgbBg(0, 255, 0))
    sbin = bytes(s, encoding="utf8")
    assert sbin == b"\x1b[38;2;255;0;0m\x1b[48;2;0;255;0m"



# Generated at 2022-06-14 08:25:37.570699
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    pass

# Generated at 2022-06-14 08:25:39.247843
# Unit test for constructor of class Register
def test_Register():
    a = Register()
    assert isinstance(a, Register)

# Generated at 2022-06-14 08:25:45.505584
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    some_class = Register()
    some_class.set_eightbit_call(RenderType.SGR)

    some_class.some_style = Style(RenderType.SGR(1))
    assert some_class.some_style == "\033[1m"

    some_class.mute()
    assert some_class.some_style == ""

    some_class.unmute()
    assert some_class.some_style == "\033[1m"


# Generated at 2022-06-14 08:25:58.671838
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    d = Register().as_dict()
    assert isinstance(d, dict)


# Generated at 2022-06-14 08:26:07.078353
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    class MyRenderType(RenderType):
        pass

    class MyOtherRenderType(RenderType):
        pass

    def myfunc(*args, **kwargs):
        return "myfunc"

    def myotherfunc(*args, **kwargs):
        return "myotherfunc"

    r = Register()
    r.set_renderfunc(MyRenderType, myfunc)
    r.set_renderfunc(MyOtherRenderType, myotherfunc)

    r.set_eightbit_call(MyRenderType)
    assert r.eightbit_call.__name__ == "myfunc"
    assert r(42) == "myfunc"
    assert r(10, 10, 10) == ""

    assert r.as_dict() == {}

    r.blue = Style(MyRenderType(0))

# Generated at 2022-06-14 08:26:10.969452
# Unit test for method unmute of class Register
def test_Register_unmute():
    a = Register()
    b = a.copy()
    b.unmute()
    assert a != b
    c = b.copy()
    c.unmute()
    assert b == c


# Generated at 2022-06-14 08:26:15.016389
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    register = Register()  # Sty().fg
    d = register.as_dict()
    nt = register.as_namedtuple()
    # check if namedtuple contains all items of dict
    for key in d:
        assert key in nt._fields
    # check if namedtuple values are equal to dict values
    for key, val in d.items():
        assert getattr(nt, key) == val

# Generated at 2022-06-14 08:26:16.678844
# Unit test for constructor of class Register
def test_Register():
    register = Register()
    assert register.is_muted == False


# Generated at 2022-06-14 08:26:30.668292
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    from . import rendertypes as R

    fg = Register()
    fg.renderfuncs.update({R.RgbFg: lambda *args: f"RgbFg {args[0]}, {args[1]}, {args[2]}" })

    fg.red = Style(R.RgbFg(255,0,0))
    assert fg.red == Style(R.RgbFg(255,0,0), value="RgbFg 255, 0, 0")

    fg.red_bold = Style(R.RgbFg(255,0,0), R.Sgr(1))

# Generated at 2022-06-14 08:26:32.577459
# Unit test for method unmute of class Register
def test_Register_unmute():

    import sty

    assert sty.Register().unmute() is None


# Generated at 2022-06-14 08:26:43.467792
# Unit test for method unmute of class Register
def test_Register_unmute():
    # Arrange
    import sty

    # Act
    fg = sty.Register()
    fg.red = Style(fg.sgr.red)
    fg.mute()
    fg.unmute()

    # Assert
    assert str(fg.red) == "\x1b[31m"

test_Register_unmute()

# Generated at 2022-06-14 08:26:50.340854
# Unit test for constructor of class Style
def test_Style():
    # Arrange:

    rule = NamedTuple("Test", [("arg", str)])
    rule_type = type(rule)
    rules = (rule(arg="a"), rule(arg="b"))

    # Act:
    s = Style(*rules)

    # Assert:
    assert isinstance(s, Style)

    assert s.rules == rules

    assert getattr(s, "rules") == rules



# Generated at 2022-06-14 08:26:59.042552
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    from .rendertype import Sgr
    from .register import Renderfuncs
    from .register import Register

    renderfuncs: Renderfuncs = {}

    def renderfunc(param: int) -> str:
        return "A"

    renderfuncs.update({Sgr: renderfunc})

    reg = Register()
    reg.set_renderfunc(Sgr, renderfunc)
    reg.set_eightbit_call(Sgr)
    assert reg(1) == "A"


# Generated at 2022-06-14 08:27:09.735182
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from .rendertype import RgbFg

    r1 = Register()
    s = Style(RgbFg(10, 20, 30), "foo")
    r1.foo = s

    s = Style(RgbFg(10, 20, 30), "bar")
    r1.bar = s

    s = Style(RgbFg(10, 20, 30), "baz")
    r1.baz = s

    assert r1.foo == "\x1b[38;2;10;20;30mfoo"
    assert r1.bar == "\x1b[38;2;10;20;30mbar"
    assert r1.baz == "\x1b[38;2;10;20;30mbaz"

    r1.set_rgb_call(RgbFg)


# Generated at 2022-06-14 08:27:21.121585
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from .rendertype import RgbBg
    from .rendertype import RgbFg

    def f1(*args, **kwargs):
        return "bg_rgb"

    def f2(*args, **kwargs):
        return "fg_rgb"

    r = Register()
    r.set_rgb_call(rendertype=RgbBg)
    r.set_renderfunc(RgbBg, f1)
    r.set_renderfunc(RgbFg, f2)

    assert r(10, 20, 30) == "bg_rgb"
    assert r(244, 255, 0) == "bg_rgb"

    r.set_rgb_call(rendertype=RgbFg)
    assert r(10, 20, 30) == "fg_rgb"
    assert r

# Generated at 2022-06-14 08:27:28.549139
# Unit test for method mute of class Register
def test_Register_mute():

    from sty import fg

    # fg.red (will be) '\x1b[31m'
    assert str(fg.red) == '\x1b[31m'

    fg.mute()
    assert not str(fg.red)

    fg.unmute()
    assert str(fg.red) == '\x1b[31m'



# Generated at 2022-06-14 08:27:39.244080
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    """
    Unit test for method as_namedtuple of class Register
    """
    MyReg = Register()

    MyReg.black = Style(RgbFg(0, 0, 0))
    MyReg.green = Style(RgbFg(0, 255, 0))
    MyReg.red = Style(RgbFg(255, 0, 0))

    TestNamedTuple = MyReg.as_namedtuple()

    assert TestNamedTuple.black == "\x1b[38;2;0;0;0m"
    assert TestNamedTuple.green == "\x1b[38;2;0;255;0m"
    assert TestNamedTuple.red == "\x1b[38;2;255;0;0m"


# Generated at 2022-06-14 08:27:51.613068
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    RegisterList = NamedTuple("RegisterList", [("fg", str), ("bg", str), ("ef", str), ("rs", str)])
    # Create register objects

    fg: Register = Register()
    bg: Register = Register()
    ef: Register = Register()
    rs: Register = Register()

    # Create styles

    fg.orange = Style("orange")
    fg.red = Style("red")
    fg.green = Style("green")
    fg.magenta = Style("magenta")
    fg.yellow = Style("yellow")
    fg.blue = Style("blue")
    fg.cyan = Style("cyan")
    fg.white = Style("white")

    bg.orange = Style("orange")
    bg.red = Style("red")
    bg.green

# Generated at 2022-06-14 08:27:53.698503
# Unit test for constructor of class Register
def test_Register():

    new_reg = Register()

    assert isinstance(new_reg, Register)


# Generated at 2022-06-14 08:28:05.517382
# Unit test for method copy of class Register
def test_Register_copy():
    register = Register()
    register.set_rgb_call(RgbFg)
    register.red = Style(RgbFg(3, 4, 5))
    other_register = register.copy()
    assert other_register.red == register.red
    assert other_register.is_muted == register.is_muted
    assert other_register.rgb_call is register.rgb_call
    other_register.red = Style(RgbFg(1, 2, 3))
    assert other_register.red != register.red
    other_register.mute()
    assert other_register.red != register.red
    assert other_register.red != Style(RgbFg(1, 2, 3))
    assert other_register.is_muted is not register.is_muted



# Generated at 2022-06-14 08:28:20.400349
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class R1(RenderType):
        pass

    class R2(RenderType):
        pass

    r = Register()
    r.set_renderfunc(R1, f1)
    r.set_renderfunc(R2, f2)

    for k, v in r.renderfuncs.items():
        if k == R1:
            assert v == f1
        elif k == R2:
            assert v == f2
        else:
            assert False



# Generated at 2022-06-14 08:28:30.783464
# Unit test for method mute of class Register
def test_Register_mute():
    # Create a register and make it muted.
    r1 = Register()
    r1.mute()
    r1.yello = Style(RgbFg(255, 255, 0))

    # The register should now be muted and the style 'yello' must be an empty
    # string.
    assert r1.is_muted == True
    assert str(r1.yello) == ""

    # After unmuting, the register should still be an str, but it should now
    # be an empty string.
    r1.unmute()
    assert r1.is_muted == False
    assert str(r1.yello) != ""
    assert isinstance(r1.yello, str) == True

# Generated at 2022-06-14 08:28:34.460172
# Unit test for method __new__ of class Style
def test_Style___new__():
    s = Style(rgb=1, bold=2)
    assert type(s) is Style
    assert s.rgb == 1
    assert s.bold == 2


# Generated at 2022-06-14 08:28:48.447130
# Unit test for method __new__ of class Style
def test_Style___new__():
    """
    This tests if the method __new__ of class Style works as expected.
    """
    import pytest
    from sty.rendertype import RgbFg, RgbBg, RgbEf, SgrBold
    from sty.colors import Red, Green, Blue
    from sty.ansi import Rgb, EightBit, Sgr

    with pytest.raises(ValueError) as e_info:
        _ = Style("Ooops")
    assert str(e_info.value) == "Parameter 'rules' must be of type Iterable[Rule]."

    red_1 = Style(RgbFg(255, 0, 0), SgrBold())
    assert isinstance(red_1, Style)

# Generated at 2022-06-14 08:28:55.789997
# Unit test for method unmute of class Register
def test_Register_unmute():

    register = Register()
    setattr(register, "red", Style(RgbFg(255, 0, 0)))

    assert register.red == "\x1b[38;2;255;0;0m"

    register.mute()

    assert register.red == ""

    register.unmute()

    assert register.red == "\x1b[38;2;255;0;0m"

# Generated at 2022-06-14 08:29:02.759486
# Unit test for method __new__ of class Style
def test_Style___new__():
    class MockAnsi(RenderType):
        def __init__(self, attribute: str, mode: str) -> None:
            self.args = ("mock_ansi", "mock_mode")

    new_style = Style(MockAnsi("Foo", "Bar"), value="")
    assert new_style.rules[0] == MockAnsi("Foo", "Bar")



# Generated at 2022-06-14 08:29:07.126977
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    class Foo(RenderType):
        render_type = "Foo"

    def renderfunc(x: int) -> str:
        return str(x + 1)

    reg = Register()
    reg.set_renderfunc(Foo, renderfunc)

    reg.set_eightbit_call(Foo)

    assert reg(10) == "11"

# Generated at 2022-06-14 08:29:20.458474
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    class MockSGR(RenderType):
        """Mock for SGR"""

        as_str = ""

        def __str__(self) -> str:
            return self.as_str

    class MockRgbFg(RenderType):
        """Mock for RgbFg"""

        as_str = ""

        def __str__(self) -> str:
            return self.as_str

    class MockRgbBg(RenderType):
        """Mock for RgbBg"""

        as_str = ""

        def __str__(self) -> str:
            return self.as_str

    R = Register()  # type: ignore
    R.set_renderfunc(MockSGR, lambda x: f"sgr_func_{x}")

# Generated at 2022-06-14 08:29:28.303846
# Unit test for constructor of class Register
def test_Register():
    # Initialize register
    register = Register()

    # Check that renderfuncs is a dict
    assert isinstance(register.renderfuncs, dict)
    assert not register.renderfuncs

    # Check that is_muted is False
    assert not register.is_muted

    # Check that eightbit_call is a lambda
    assert callable(register.eightbit_call)

    # Check that rgb_call is a lambda
    assert callable(register.rgb_call)



# Generated at 2022-06-14 08:29:40.025697
# Unit test for method __new__ of class Style
def test_Style___new__():
    """
    This method tests whether a Style-object is created correctly, i.e.
    with all the right parameters.
    """
    class TestRenderType(RenderType):
        def get_code(self):
            return str(self.args)

    renderfuncs = {TestRenderType: lambda x: f"{x}"}
    rt1 = TestRenderType(1)
    rt2 = TestRenderType(2)
    rt3 = TestRenderType(3)
    rt4 = TestRenderType(4)

    s1 = Style(rt1, rt2)
    assert s1.rules == (rt1, rt2)
    assert str(s1) == "12"

    s2 = Style(rt1, s1, rt3)

# Generated at 2022-06-14 08:30:07.447283
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    from .rendertype import Sgr, RgbBg

    r1 = Register()

    # Add renderfuncs for Sgr and RgbBg.
    r1.set_renderfunc(Sgr, lambda *args: "foo")
    r1.set_renderfunc(RgbBg, lambda *args: "bar")

    # Create a style rule where the Sgr and RgbBg should be rendered.
    r1.foo = Style(Sgr(42), RgbBg(10, 20, 30))

    assert r1.foo == "foobar"

    # Change the renderfunc for RgbBg to render it as RgbFg.

# Generated at 2022-06-14 08:30:16.625212
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    cfg = Register()
    cfg.green = Style(RgbFg(0, 255, 0))

    # Get initial value for green
    initialValue = cfg.green

    def new_renderfunc(color):
        return "\x1b[38;2;{};{};{}m".format(*color)

    # Set test value
    cfg.set_renderfunc(RgbFg, new_renderfunc)

    # Get value after renderfunc changed
    newValue = cfg.green

    # Test
    assert newValue != initialValue

# Generated at 2022-06-14 08:30:25.579944
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    class Foo(Register):
        pass

    fg = Foo()

    fg.red = Style(Sgr(1), RgbFg(1, 0, 0))
    fg.blue = Style(Sgr(1), RgbFg(0, 0, 1))

    assert fg.as_dict() == {'red': '\x1b[38;2;1;0;0m\x1b[1m', 'blue': '\x1b[38;2;0;0;1m\x1b[1m'}

# Generated at 2022-06-14 08:30:37.111378
# Unit test for method unmute of class Register
def test_Register_unmute():
    """ Test if mute method successfully resets the value of muted styles."""

    class TestRegister(Register):

        def __init__(self):
            super().__init__()

            self.red = Style(RgbFg(255, 0, 0), Sgr(1))
            self.black = Style(RgbBg(0, 0, 0))
            self.redblack = Style(self.red, self.black)

    register = TestRegister()

    assert register.red == "\x1b[38;2;255;0;0m\x1b[1m"
    assert register.black == "\x1b[48;2;0;0;0m"
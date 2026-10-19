

# Generated at 2022-06-14 08:20:59.125374
# Unit test for method mute of class Register
def test_Register_mute():

    from .rendertype import Sgr
    from .sty import sty

    sty.set_renderfunc(Sgr, lambda x, sgr: "sgr" * x)

    s = sty.fg.yellow

    sty_copy = sty.copy()

    sty_copy.mute()

    sty_copy.fg.orange = s

    assert str(sty.fg.orange) == "sgrsgr"
    assert str(sty_copy.fg.orange) == ""

    sty_copy.unmute()

    sty_copy.fg.red = s

    assert str(sty.fg.red) == "sgrsgr"
    assert str(sty_copy.fg.red) == "sgrsgr"



# Generated at 2022-06-14 08:21:07.538396
# Unit test for method mute of class Register
def test_Register_mute():
    from . import RenderType, Styles
    from .rendertypes import EightbitBg, EightbitFg, RgbBg, RgbFg, Sgr
    from .styles import Styles

    # Add renderfunc for Sgr
    Styles.fg.set_renderfunc(Sgr, lambda *args: "")

    # Renderfunc for EightbitFg
    Styles.fg.set_renderfunc(EightbitFg, lambda *args: "\x1b[38;5;{}m".format(*args))

    # Renderfunc for EightbitBg
    Styles.bg.set_renderfunc(EightbitBg, lambda *args: "\x1b[48;5;{}m".format(*args))

    # Renderfunc for RgbFg

# Generated at 2022-06-14 08:21:19.533871
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    from . import RgbFg, RgbBg

    import pytest

    def add_style(reg, name, style):
        setattr(reg, name, style)

    fg, bg, ef, rs = Register(), Register(), Register(), Register()

    assert "red" not in fg.as_dict().keys()
    add_style(fg, "red", Style(RgbFg(255,0,0)))
    assert "red" in fg.as_dict().keys()

    assert "red_on_white" not in fg.as_dict().keys()
    add_style(fg, "red_on_white", Style(fg.red, bg.white))
    assert "red_on_white" in fg.as_dict().keys()

# Generated at 2022-06-14 08:21:32.285336
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    class RenderType1(RenderType):
        """
        Rendertype for testing.
        """

        def render(self, *args, **kwargs):
            return "\x1b[1;{};{};{}m".format(*args)

    class RenderType2(RenderType):
        """
        Rendertype for testing.
        """

        def render(self, *args, **kwargs):
            return "\x1b[2;{};{};{}m".format(*args)

    register = Register()

    # Define 2 renderfuncs and save them in the register object.
    renderfunc1 = lambda *args, **kwargs: RenderType1(*args, **kwargs).render()
    renderfunc2 = lambda *args, **kwargs: RenderType2(*args, **kwargs).render()
    register.set_render

# Generated at 2022-06-14 08:21:39.486905
# Unit test for method copy of class Register
def test_Register_copy():

    r = Register()
    r.test = Style(Sgr(1))

    r2 = r.copy()

    # Test if both objects are independent.
    r.test = Style(Sgr(0))
    assert r.test == "\x1b[0m"
    assert r2.test == "\x1b[1m"

    r3 = r.as_namedtuple()

    assert r3.test == "\x1b[0m"



# Generated at 2022-06-14 08:21:50.876469
# Unit test for method unmute of class Register
def test_Register_unmute():
    """
        Test method unmute of class Register.
    """
    import pytest

    # Create some rendertypes
    class Sgr(RenderType):
        args = ["n"]
        renderfunc = lambda self, n: f"\x1b[{n}m"

    class RgbFg(RenderType):
        args = ["r", "g", "b"]
        renderfunc = lambda self, r, g, b: f"\x1b[38;2;{r};{g};{b}m"

    class RgbBg(RenderType):
        args = ["r", "g", "b"]
        renderfunc = lambda self, r, g, b: f"\x1b[48;2;{r};{g};{b}m"


    # Create register object
    register = Register()



# Generated at 2022-06-14 08:21:57.866525
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    class Rgb(RenderType):
        pass

    class Ansi(RenderType):
        pass

    class Rgb2(RenderType):
        pass

    class Ansi2(RenderType):
        pass

    def render_rgb(r: int, g: int, b: int) -> str:
        return f"\x1b[38;2;{r};{g};{b}m"

    def render_ansi(code: int) -> str:
        return f"\x1b[38;5;{code}m"

    def render_rgb2(r: int, g: int, b: int) -> str:
        return f"\x1b[38;2;{r};{g};{b}m"

    def render_ansi2(code: int) -> str:
        return

# Generated at 2022-06-14 08:22:02.905998
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    from .ext.eightbit import Eightbit

    r = Register()
    r.eightbit = Style(Eightbit("1"))
    nt = r.as_namedtuple()

    assert nt.eightbit == "\x1b[38;5;1m"

# Generated at 2022-06-14 08:22:08.007958
# Unit test for method __call__ of class Register
def test_Register___call__():
    reg = Register()
    Style = namedtuple("Style", ["rules"])
    color = Style(rules=[0])
    reg.green = color
    assert reg(0) == ""
    assert reg("green") == "\x1b[38;5;2m"
    assert reg(10, 42, 255) == ""


# Generated at 2022-06-14 08:22:14.400519
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    from .rendertype import Sgr

    r: Register = Register()

    def eightbit_func(code): return "eightbit_func"
    def rgb_func(r, g, b): return "rgb_func"

    r.set_renderfunc(Sgr, eightbit_func)
    r.set_eightbit_call(Sgr)

    assert str(r(1)) == "eightbit_func"

    r.set_renderfunc(Sgr, rgb_func)
    assert str(r(1)) == "rgb_func"



# Generated at 2022-06-14 08:22:25.079928
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    class TestRegister(Register):
        def __init__(self):
            super().__init__()
            self.a = Style()
            self.b = Style()

    t = TestRegister()

    Tuple = t.as_namedtuple()

    assert isinstance(Tuple, NamedTuple)
    assert hasattr(Tuple, "a")
    assert hasattr(Tuple, "b")
    assert hasattr(Tuple, "renderfuncs")
    assert hasattr(Tuple, "is_muted")
    assert hasattr(Tuple, "eightbit_call")
    assert hasattr(Tuple, "rgb_call")

# Generated at 2022-06-14 08:22:34.773230
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    # Test Setup
    def rgb_render(r:int, g:int, b:int) -> str:
        if (r, g, b) == (10, 20, 30):
            return "Rendering red rgb"
        else:
            return "Something went wrong"

    register = Register()

    register.set_renderfunc(RgbFg, rgb_render)

    # Run test
    assert register.rgb_call(10, 20, 30) == "Rendering red rgb"


# Generated at 2022-06-14 08:22:45.849609
# Unit test for method copy of class Register
def test_Register_copy():

    class ExtendedRegister(Register):
        pass

    reg_1 = Register()
    reg_2 = ExtendedRegister()

    reg_1.set_renderfunc(RenderType, lambda x: x)
    reg_1.set_eightbit_call(RenderType)
    reg_1.set_rgb_call(RenderType)
    reg_1.test = Style(value="test")

    reg_2 = reg_1.copy()

    assert isinstance(reg_2, Register)
    assert reg_2.renderfuncs == reg_1.renderfuncs
    assert reg_2.eightbit_call == reg_1.eightbit_call
    assert reg_2.rgb_call == reg_1.rgb_call
    assert reg_2.test == reg_1.test

    reg_3 = reg_1.copy

# Generated at 2022-06-14 08:22:55.319263
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    """
    Unit test for method ``set_eightbit_call``.
    """
    from .rendertype import RgbFg

    def call(n):
        return f"\x1b[38;2;{n*4};{n*2};{n}"

    reg = Register()
    reg.set_renderfunc(RgbFg, call)
    reg.set_eightbit_call(RgbFg)
    assert reg(2) == "\x1b[38;2;8;4;2"


# Generated at 2022-06-14 08:23:03.227415
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    reg = Register()
    dct = {"background": "background", "foreground": "foreground", "effect": "effect", "reset": "reset"}
    reg.background = "background"
    reg.foreground = "foreground"
    reg.effect = "effect"
    reg.reset = "reset"
    names_reg = reg.as_namedtuple()._asdict()
    assert all(k in names_reg for k in dct)


# Generated at 2022-06-14 08:23:09.058695
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    from .rendertype import Sgr

    class TestRegister(Register):
        pass

    r = TestRegister()
    r.set_eightbit_call(Sgr)
    r.set_renderfunc(Sgr, lambda x: f"SGR({x})")
    assert r(1) == "SGR(1)"

# Generated at 2022-06-14 08:23:13.589322
# Unit test for method unmute of class Register
def test_Register_unmute():

    from .defaults import fg

    assert not fg.is_muted
    fg.mute()
    assert fg.is_muted
    fg.unmute()
    assert not fg.is_muted

# Generated at 2022-06-14 08:23:17.617855
# Unit test for method __new__ of class Style
def test_Style___new__():
    from .sgr import Sgr

    s = Style(Sgr(1))

    assert isinstance(s, Style)
    assert isinstance(s, str)
    assert str(s) == "\x1b[1m"



# Generated at 2022-06-14 08:23:27.799930
# Unit test for constructor of class Style
def test_Style():
    Style(value="foo")
    Style(*[1, 2, 3], value="foo")
    Style(1, 2, 3, value="foo")
    Style(1, 2, *[3], value="foo")
    #Style(1, 2, 3, foo="bar")
    #Style(1, 2, 3, value="foo", bar="baz")
    #Style(1, 2, value="foo", bar="baz")
    Style(value="foo", bar="baz")
    #Style(1, value="foo", bar="baz")
    Style(1, value="foo")



# Generated at 2022-06-14 08:23:30.920497
# Unit test for method __call__ of class Register
def test_Register___call__():

    r = Register()
    r.red = Style(RgbFg(255, 0, 0))

    assert r(255, 0, 0) == r.red

# Generated at 2022-06-14 08:23:41.415190
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    new_register = Register()
    new_register.hello = Style(RenderType)
    new_register.world = Style(RenderType)
    assert hasattr(new_register.as_namedtuple(), "hello")
    assert hasattr(new_register.as_namedtuple(), "world")
    # TODO Enhance this test.


# Generated at 2022-06-14 08:23:52.998001
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    r = Register()
    r.yellow = Style(RenderType.f256(4))
    r.red = Style(RenderType.f256(1))
    r.set_eightbit_call(RenderType.f256)
    r.set_rgb_call(RenderType.rgb)

    assert r.red == "\x1b[38;5;1m", r.red
    assert r.yellow == "\x1b[38;5;4m", r.yellow
    assert r(144) == "\x1b[38;5;144m", r(144)
    assert r(10, 42, 240) == "\x1b[38;2;10;42;240m", r(10, 42, 240)


# Test for method Register.mute

# Generated at 2022-06-14 08:24:05.150471
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .sty import Sty
    sty = Sty(True)
    sty.setup_default_register()

    sty.fg.set_eightbit_call(sty.rendertypes.SgrFg)

    assert sty.fg(255) == "\x1b[38;5;255m"

    sty.fg.set_eightbit_call(sty.rendertypes.RgbFg)

    assert sty.fg(255) == "\x1b[38;2;255;255;255m"

    sty.fg.set_rgb_call(sty.rendertypes.SgrFg)

    assert sty.fg(255, 127, 0) == "\x1b[38;2;255;127;0m"

    sty.fg.set_rgb_call(sty.rendertypes.RgbFg)


# Generated at 2022-06-14 08:24:17.351777
# Unit test for method copy of class Register
def test_Register_copy():
    """
    Test if the deepcopy of a  Register-object works as expected.
    """
    from .utils import clear_registers

    register = Register()
    register.red = Style(RenderType(), RenderType())
    register.blue = Style(RenderType())
    register.green = Style(RenderType(), RenderType())

    copy = register.copy()

    assert copy is not register

    assert copy.red is not register.red
    assert copy.blue is not register.blue
    assert copy.green is not register.green

    copy.red = Style(RenderType())
    copy.green = Style(RenderType())
    copy.blue = Style(RenderType())

    assert copy.red != register.red
    assert copy.green != register.green
    assert copy.blue != register.blue

    copy.__del__()
    register

# Generated at 2022-06-14 08:24:26.187001
# Unit test for method mute of class Register
def test_Register_mute():

    from .registers import (
        FgBg,
        EightBit,
        Rgb,
        Sgr,
        fg,
        bg,
    )

    def eightbit_renderfunc(x: int) -> str:
        return f"\x1b[{x}m"

    def rgb_renderfunc(r: int, g: int, b: int) -> str:
        return f"\x1b[38;2;{r};{g};{b}m"

    # Create some styling rules
    fg_blue = FgBg(94)
    fg_red = FgBg(196)
    sgr_bold = Sgr(1)
    render_rule = EightBit(100)

    # Create styles
    blue = Style(fg_blue)
    red = Style

# Generated at 2022-06-14 08:24:29.791733
# Unit test for method unmute of class Register
def test_Register_unmute():

    from .ef import ef

    ef_copy = ef.copy()

    ef.mute()
    test_1 = Style(ef.blinking_off)

    ef.unmute()
    test_2 = Style(ef.blinking_off)

    assert test_1 == ""
    assert test_2 == "\x1b[25m"

    # Restore default state
    setattr(ef, 'blinking_off', test_2)



# Generated at 2022-06-14 08:24:35.606155
# Unit test for method __call__ of class Register
def test_Register___call__():
    r = Register()
    r.eightbit = Style(RgbFg(1, 5, 10))
    assert r(10) == "\x1b[38;2;1;5;10m"
    assert r("eightbit") == "\x1b[38;2;1;5;10m"
    assert r() == ""

# Generated at 2022-06-14 08:24:42.228618
# Unit test for method __call__ of class Register
def test_Register___call__():

    from .const import fg, bg, ef, rs
    from .rendertype import RgbBg, RgbFg, Sgr

    assert fg(1) == "\x1b[38;5;1m"
    assert bg(1) == "\x1b[48;5;1m"
    assert fg(42, 240, 101) == "\x1b[38;2;42;240;101m"
    assert fg("red") == "\x1b[31m"

    ef.bold = Style(Sgr(1))

    assert str(ef.bold) == "\x1b[1m"

    bg.red = Style(RgbBg(255, 0, 0))

    assert bg.red == "\x1b[48;2;255;0;0m"



# Generated at 2022-06-14 08:24:55.335177
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    from . import ef, rs, Sgr, SgrFg
    from .rendertype import RenderType
    from .rendertype.sgr import RgbFg

    def the_func():
        return "42"

    ef_copy = ef.copy()
    ef_copy.set_renderfunc(SgrFg, the_func)
    assert callable(ef_copy.renderfuncs[SgrFg])
    assert ef_copy.renderfuncs[SgrFg]() == "42"

    ef_copy.set_renderfunc(SgrFg, lambda: "21")
    assert ef_copy.renderfuncs[SgrFg]() == "21"

    ef_copy.set_renderfunc(RgbFg, the_func)

# Generated at 2022-06-14 08:25:02.773194
# Unit test for method copy of class Register
def test_Register_copy():

    # Create register
    register = Register()

    # Create 'reset' style
    style = Style(Sgr(0))

    # Add 'reset' style
    register.reset = style

    # Create copy
    register_copy = register.copy()

    # Change 'reset' style in copy
    register_copy.reset = Style(Sgr(1))

    # Check if 'reset' style in register is changed
    assert register.reset == Style(Sgr(0))



# Generated at 2022-06-14 08:25:26.411451
# Unit test for method unmute of class Register
def test_Register_unmute():
    from sys import stdout
    from .sgr import Sgr
    from .fg import Fg
    from .eightbit import Eightbit
    from .rgb import RgbFg
    from .namedcolors import NamedColors

    # Create a new register object
    r: Register = Register()
    r.set_eightbit_call(Eightbit)
    r.set_rgb_call(RgbFg)

    # Define a render function for Sgr-rules
    def func(val):
        return f"\x1b[{val}m"
    r.set_renderfunc(Sgr, func)

    # Define a render function for RGB-rules
    def func(r, g, b):
        return f"\x1b[38;2;{r};{g};{b}m"
   

# Generated at 2022-06-14 08:25:36.546178
# Unit test for method mute of class Register
def test_Register_mute():
    """
    Test ``mute`` method.
    """
    class _X(Register):
        def __init__(self, name: str, value: str):
            self.name = name
            self.value = value

        def __len__(self):
            return 0

    x = _X("name", Style("value"))
    x.mute()
    assert x.is_muted == True
    assert x.value == ""
    x.unmute()
    assert x.is_muted == False
    assert x.value == "value"
    assert str(x) == "value"


# Generated at 2022-06-14 08:25:42.301705
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():

    class TestRegister(Register):
        def __init__(self):
            super().__init__()

        test = Style(Sgr(1))

    registers = TestRegister()

    result = registers.as_namedtuple()

    assert type(result) == namedtuple("StyleRegister", "test")
    assert result.test == "\x1b[1m"



# Generated at 2022-06-14 08:25:49.863765
# Unit test for method __new__ of class Style
def test_Style___new__():

    from .rendertype import RgbFg, NoFg, Sgr

    # -------------------------
    # Default case
    # -------------------------
    a = Style(RgbFg(1, 2, 3), Sgr(1))

    assert str(a) == "\x1b[38;2;1;2;3m\x1b[1m"
    assert a.rules == (RgbFg(1, 2, 3), Sgr(1))

    # -------------------------
    # Value
    # -------------------------
    a = Style(RgbFg(1, 2, 3), Sgr(1), value="test")

    assert str(a) == "test"
    assert a.rules == (RgbFg(1, 2, 3), Sgr(1))

test_Style___new__()



# Generated at 2022-06-14 08:26:00.299200
# Unit test for constructor of class Register
def test_Register():
    reg = Register()

    # Check object creation
    assert isinstance(reg, Register) is True

    # Check default render functions
    assert "eightbit" in reg.renderfuncs
    assert isinstance(reg.renderfuncs["eightbit"], Callable) is True
    assert "rgb" in reg.renderfuncs
    assert isinstance(reg.renderfuncs["rgb"], Callable) is True

    # Check default render calls
    assert reg.eightbit_call is not None
    assert isinstance(reg.eightbit_call, Callable) is True
    assert reg.rgb_call is not None
    assert isinstance(reg.rgb_call, Callable) is True



# Generated at 2022-06-14 08:26:13.752410
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    import sty

    Sty = sty.Styler()
    Sty.config.register_box = sty.Register()
    Sty.config.register_box.set_renderfunc(sty.rendertype.Sgr, lambda x: f"\x1b[{x}m")
    Sty.config.register_box.bold = sty.Style(sty.rendertype.Sgr(1))
    Sty.config.register_box.bold.rules.append(sty.rendertype.Sgr(2))
    Sty.config.register_box.bold.rules.append(sty.rendertype.Sgr(3))

    assert str(Sty.config.register_box.bold) == "\x1b[1m\x1b[2m\x1b[3m"



# Generated at 2022-06-14 08:26:19.178007
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    from .default import fg, bg

    ntuple = bg.as_namedtuple()
    assert ntuple.black == '\x1b[48m' # Black should be first attribute of ntuple object

    ntuple = fg.as_namedtuple()
    assert ntuple.white == '\x1b[38;2;255;255;255m' # White should be first attribute of ntuple object

# Generated at 2022-06-14 08:26:32.011778
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    from sty.fmt import RgbFg, Sgr
    from sty.muted import Muted

    r1 = Register()
    r2 = Register()
    r2.is_muted = True

    r1.test1 = Style(Sgr(1))
    r2.test1 = Style(Sgr(1))

    r1.test2 = Style(RgbFg(1, 2, 3), Sgr(1))
    r2.test2 = Style(RgbFg(1, 2, 3), Sgr(1))

    assert getattr(r1, "test1") == "\x1b[1m"
    assert getattr(r1, "test2") == "\x1b[38;2;1;2;3m\x1b[1m"


# Generated at 2022-06-14 08:26:45.396654
# Unit test for method __call__ of class Register
def test_Register___call__():

    reg = Register()
    reg.red = Style(RgbFg(255, 0, 0))

    assert reg(255, 0, 0) == ""
    assert reg("red") == ""

    reg = Register()
    reg.red = Style(RgbFg(255, 0, 0))

    class DummyRender:
        def __call__(self, x):
            return "DummyRender"

    reg2 = reg.copy()

    reg.red = Style(RgbFg(0, 255, 0))
    reg.set_renderfunc(RgbFg, DummyRender())
    reg.set_rgb_call(RgbFg)

    assert reg("red") == "DummyRender"

    reg2.red = Style(RgbFg(0, 0, 255))
    reg2.set_

# Generated at 2022-06-14 08:26:53.486162
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    """
    The method ``__setattr__`` is a little bit special. It is called when a value
    is assigned to an attribute. Since this method is called without the object
    (``self``) as the first parameter, we need to override the method
    ``__setattr__`` here to be able to pass ``self``.
    """

    def _setattr(self, name: str, value: Style):
        return super().__setattr__(name, value)

    reg = Register()
    current_setattr = reg.__setattr__
    reg.__setattr__ = _setattr

    from .rendertype import Sgr, RgbFg

    reg.foo = Style(Sgr(1), RgbFg(10, 100, 255))

    assert isinstance(reg.foo, Style)

# Generated at 2022-06-14 08:27:28.611032
# Unit test for method copy of class Register
def test_Register_copy():
    fg = Register()
    fg  # do something with fg
    fg2 = fg.copy()
    assert(isinstance(fg2, Register))
    fg3 = fg.copy()
    assert(isinstance(fg3, Register))
    fg4 = fg.copy()
    assert(isinstance(fg4, Register))



# Generated at 2022-06-14 08:27:39.473851
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    from .rendertype import Intensity, RgbBg, RgbFg, Reset, Sgr

    x = Register()
    x.black = Style(Sgr(0), RgbFg(0, 0, 0))
    x.red = Style(RgbFg(255, 0, 0), Intensity(2))
    x.bg_red = Style(RgbBg(255, 0, 0))
    x.reset = Style(Reset())

    t = x.as_namedtuple()

    assert t.black == "\x1b[38;2;0;0;0m"
    assert t.red == "\x1b[38;2;255;0;0m\x1b[2m"
    assert t.bg_red == "\x1b[48;2;255;0;0m"

# Generated at 2022-06-14 08:27:42.552548
# Unit test for method __new__ of class Style
def test_Style___new__():
    style = Style()

    assert isinstance(Style(), Style)
    assert isinstance(Style(), str)
    assert style == ""
    assert style.rules == ()


# Generated at 2022-06-14 08:27:54.217459
# Unit test for method copy of class Register

# Generated at 2022-06-14 08:28:07.737292
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    class ExtendRegister(Register):

        fg = Style(RgbFg(5, 5, 5))

    r1 = ExtendRegister()

    for rt1 in (RgbFg, None):
        for rt2 in (RgbFg, None):

            r1.set_rgb_call(rt1)
            r2 = r1.copy()
            r2.set_rgb_call(rt2)

            if rt1:
                assert r1.rgb_call.__name__ == rt1.__name__
            else:
                assert r1.rgb_call.__name__ != rt1.__name__

            if rt2:
                assert r2.rgb_call.__name__ == rt2.__name__
            else:
                assert r2.rgb

# Generated at 2022-06-14 08:28:19.038174
# Unit test for constructor of class Register
def test_Register():
    from .rendertype import DCS, Sgr, RgbFg, RgbBg, Csi

    def renderfunc(x: int) -> str:
        return "2;{x}".format(x=x)

    x: Register = Register()
    x.set_renderfunc(DCS, renderfunc)

    x.test_style = Style(DCS(1), Sgr(1))
    x.test_style2 = Style(DCS(2))

    y: Register = x.copy()

    assert not isinstance(x, str) and not isinstance(y, str)
    assert isinstance(x.test_style, str) and isinstance(y.test_style, str)
    assert x.test_style is not y.test_style
    assert x.renderfuncs == y.renderfuncs

# Generated at 2022-06-14 08:28:31.420193
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .rendertype import Eightbit, Rgb

    t: Register = Register()
    t.set_eightbit_call(Eightbit)
    t.set_rgb_call(Rgb)

    t.red = Style(Eightbit(1))
    t.green = Style(Eightbit(2))
    t.blue = Style(Rgb(1, 2, 3))

    assert t("red") == "\x1b[38;5;1m"
    assert t("green") == "\x1b[38;5;2m"
    assert t("blue") == "\x1b[38;2;1;2;3m"

    assert t(1) == "\x1b[38;5;1m"
    assert t(2) == "\x1b[38;5;2m"

# Generated at 2022-06-14 08:28:35.627747
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    r = Register()
    r.set_renderfunc(str, lambda x: "Hello " + x)
    r.set_eightbit_call(str)
    assert r("World") == "Hello World"

# Generated at 2022-06-14 08:28:41.012818
# Unit test for method mute of class Register
def test_Register_mute():
    from .rendertype import Sgr
    from .fg import Fg

    fg = Fg()
    fg.red = Style(Sgr(1))

    fg.mute()
    assert "m" == fg("red")



# Generated at 2022-06-14 08:28:51.116306
# Unit test for method copy of class Register
def test_Register_copy():
    import sty

    register = sty.Register()
    register.a = sty.Style(sty.RgbFg(255, 0, 0))
    register.b = sty.Style(sty.RgbFg(0, 255, 0))

    assert register.a == "\x1b[38;2;255;0;0m"
    assert register.b == "\x1b[38;2;0;255;0m"

    ob2 = register.copy()
    ob2.a = sty.Style(sty.RgbFg(0, 0, 255))

    assert register.a == "\x1b[38;2;255;0;0m"
    assert register.b == "\x1b[38;2;0;255;0m"

# Generated at 2022-06-14 08:29:30.439884
# Unit test for method mute of class Register
def test_Register_mute():

    r = Register()

    r.test1 = Style(RgbFg(1, 1, 1))
    r.test2 = Style(RgbFg(1, 1, 1))

    t1 = r.test1
    t2 = r.test2

    assert t1 is not t2

    r.mute()

    t3 = r.test1
    t4 = r.test2

    assert t1 == t3
    assert t2 == t4
    assert t3 is t4

# Generated at 2022-06-14 08:29:38.406044
# Unit test for method copy of class Register
def test_Register_copy():
    from .rendertype import RgbBg, RgbFg
    from .registers import fg

    fg.orange = Style(RgbFg(1,5,10))
    fg_copy = fg.copy()

    # Check if fg is not the same object as fg_copy.
    assert id(fg) != id(fg_copy)

    # Check if fg.orange is not the same object as fg_copy.orange.
    assert id(fg.orange) != id(fg_copy.orange)



# Generated at 2022-06-14 08:29:49.371251
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    reg = Register()
    def renderfunc1(x):
        return ""

    def renderfunc2(x, y):
        return ""

    reg.set_renderfunc(RenderType, renderfunc1)
    reg.set_renderfunc(NamedTuple, renderfunc2)

    reg.test = Style(NamedTuple(1, 2), RenderType(1))
    reg.test2 = Style(NamedTuple(3, 4), RenderType(10))

    assert len(reg.test.rules) == 2
    assert isinstance(reg.test.rules[0], NamedTuple)
    assert isinstance(reg.test.rules[1], RenderType)

    assert len(reg.test2.rules) == 2
    assert isinstance(reg.test2.rules[0], NamedTuple)

# Generated at 2022-06-14 08:29:54.641066
# Unit test for method copy of class Register
def test_Register_copy():

    # Create reg and make a copy of it
    reg = Register()
    reg.a = Style(1, 2, 3)
    reg.b = Style(4, 5)
    reg_copy = reg.copy()

    # Change something in reg. This should not affect reg_copy
    reg.a = Style(8, 9, 10)

    assert reg_copy.a != reg.a

# Generated at 2022-06-14 08:30:00.668397
# Unit test for method mute of class Register
def test_Register_mute():

    def renderfunc(x):
        return str(x)

    r = Register()
    r.set_renderfunc(RgbBg, renderfunc)
    r.bg.red = RgbBg(1, 0, 0)
    r.mute()
    assert r.bg.red == ""



# Generated at 2022-06-14 08:30:13.213439
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    from .default_register import fg

    from .rendertype import RgbFg


# Generated at 2022-06-14 08:30:21.546026
# Unit test for method copy of class Register
def test_Register_copy():
    # Create a Register object and add some "styles" to it
    r1 = Register()
    r1.foo = Style(value="foo")
    r1.bar = Style(value="bar")

    # Make a copy of the Register object
    r2 = r1.copy()

    # Test if the "styles" are also present in the copy
    assert r2.foo == "foo"
    assert r2.bar == "bar"

# Generated at 2022-06-14 08:30:28.817418
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert len(r.__dict__) == 3
    assert r.__dict__["renderfuncs"] == {}
    assert r.__dict__["is_muted"] is False
    assert r.__dict__["eightbit_call"] == r.eightbit_call
    assert r.__dict__["rgb_call"] == r.rgb_call

# Generated at 2022-06-14 08:30:38.002885
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():

    from .rendertype import RgbFg, AssortedFg, AssortedBg

    import sys, os

    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

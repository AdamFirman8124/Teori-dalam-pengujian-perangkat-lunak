

# Generated at 2022-06-14 08:21:00.411364
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    def r1(arg1: str, arg2: int, arg3: str) -> str:
        return f"{arg1}:{arg2}:{arg3}"

    def r2(arg1: str) -> str:
        return f"{arg1}"

    def r3(arg1: int) -> str:
        return f"{arg1}"

    rendertype1 = RenderType("type1", str, int, str)
    rendertype2 = RenderType("type2", str)
    rendertype3 = RenderType("type3", int)

    Sty = Register()
    Sty.set_renderfunc(rendertype1, r1)
    Sty.set_renderfunc(rendertype2, r2)

    assert Sty.renderfuncs == {rendertype1: r1, rendertype2: r2}

    Sty.set

# Generated at 2022-06-14 08:21:08.809202
# Unit test for method unmute of class Register
def test_Register_unmute():

    from .style import style

    style.reset()
    register: Register = Register()
    register.set_renderfunc(RenderType, lambda x: "test")
    register.test = Style(RenderType())
    assert register.test == "test"

    register.mute()

    assert register.test == ""
    register.unmute()  # This method call is important for the test.
    assert register.test == "test"
    style.reset()



# Generated at 2022-06-14 08:21:20.383184
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    from .ansi import CsiFg, CsiBg
    from .sty import Sty

    def render_styled_text(sty, text):
        """
        This function is the "renderfunc" and gets assigned to the CsiFg rendertype.
        """
        return f"{sty.fg.red}{text}{sty.rs.all}"

    sty = Sty()

    # Add render-func for rendertype CsiFg.
    sty.fg.set_renderfunc(CsiFg, render_styled_text)

    # Check if renderfunc has been set correctly.
    assert(sty.fg.renderfuncs[CsiFg] == render_styled_text)

    # Check if renderfunc has been set to eightbit call.

# Generated at 2022-06-14 08:21:33.292667
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class Rgb(RenderType):
        args = 3
        code = 38

    class Sgr(RenderType):
        args = 1
        code = "m"
        # TODO: Gui, is the code here a string???

    def render_Rgb(r: int, g: int, b: int) -> str:
        return f"\x1b[38;2;{r};{g};{b}m"

    def render_Sgr(n: int) -> str:
        return f"\x1b[{n}m"

    my_register = Register()
    my_register.set_renderfunc(Rgb, render_Rgb)
    my_register.set_renderfunc(Sgr, render_Sgr)


# Generated at 2022-06-14 08:21:38.974828
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    sty = Register()
    sty.set_renderfunc(str, lambda x: "abc")
    sty.set_eightbit_call(str)
    sty.set_rgb_call(str)

    # assert sty.eightbit_call(1) == "abc"
    # assert sty.rgb_call(1, 2, 3) == "abc"



# Generated at 2022-06-14 08:21:43.319574
# Unit test for method unmute of class Register
def test_Register_unmute():
    register = Register()
    register.set_rgb_call(RenderType.RgbFg)
    setattr(register, "red", Style(RenderType.RgbFg(255,0,0)))

    # test for NoneError when unmuting the first time
    register.unmute()



# Generated at 2022-06-14 08:21:53.990386
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    """
    Test the method Register.set_renderfunc().
    """
    from .rendertype import Sgr
    from .render import SgrRender

    # Register with default values
    r0 = Register()

    # Check default renderfunc
    assert r0.renderfuncs[Sgr].__name__ == SgrRender.__name__

    # Define a new renderfunc
    def f1(*args):
        return "Dummy"

    # Set new renderfunc
    r0.set_renderfunc(Sgr, f1)

    # Check new renderfunc
    assert r0.renderfuncs[Sgr].__name__ == f1.__name__

    # Define styles
    r0.style1 = Style(Sgr(1))
    r0.style2 = Style(Sgr(2))
    r0.style

# Generated at 2022-06-14 08:22:01.719939
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    # Init parameters
    rendertype: Type[RenderType] = RenderType
    func: Callable = lambda x: x

    # Init object with empty dict
    r: Register = Register()
    r.renderfuncs: Renderfuncs = {}

    # Set new renderfunc
    r.set_renderfunc(rendertype, func)

    # Compare renderfuncs
    assert r.renderfuncs == {rendertype: func}


# Generated at 2022-06-14 08:22:08.783835
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    r = Register()
    r.foobar = Style(Sgr(1))

    # Check if attribute foobar is None
    assert r.foobar is None

    # Add renderfunc for Sgr
    r.set_renderfunc(Sgr, lambda x: 42)

    # Check if attribute foobar is 42 after adding renderfunc
    assert r.foobar == "42"

# Generated at 2022-06-14 08:22:16.549027
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class TestRegister(Register):
        pass

    # Create register
    register = TestRegister()
    # Add render-func
    register.set_renderfunc(rendertype=object, func=lambda: "hello")

    # Check if renderfunc was added correctly
    assert "hello" == register.renderfuncs[object]()

    # Check if renderfunc is correctly returned.
    assert register._get_renderfunc(rendertype=object)() == "hello"

# Generated at 2022-06-14 08:22:27.724605
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class ColorCodes(NamedTuple):
        fg: str
        bg: str

    def func_1(n):
        return ColorCodes(f"F{n}", f"B{n}")

    def func_2(n):
        return ColorCodes(f"F{n+1}", f"B{n+1}")

    class Foo(RenderType):
        CODE = 33

    foo1 = Register()
    foo1.set_renderfunc(Foo, func_1)

    # Set a new renderfunc
    foo2 = foo1.copy()
    foo2.set_renderfunc(Foo, func_2)

    # Call a style
    s = foo2.green

    assert (s.rules == (Foo(22),))

# Generated at 2022-06-14 08:22:41.454604
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    from .rendertype import RgbBg, EightBitBg

    def eightbit(bg: int) -> str:
        return f"\x1b[48;5;{bg}m"

    def rgb(bg: int, *args) -> str:
        return f"\x1b[48;2;{bg};{args[0]};{args[1]}m"

    register = Register()
    register.set_renderfunc(EightBitBg, eightbit)
    register.set_renderfunc(RgbBg, rgb)

    assert str(register(100)) == "\x1b[48;5;100m"
    assert str(register(100, 200, 250)) == "\x1b[48;2;100;200;250m"



# Generated at 2022-06-14 08:22:48.911921
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    def RenderType1(self):
        return "RenderType1"

    def RenderType2(self):
        return "RenderType2"

    def RenderType3(self):
        return "RenderType3"

    register = Register()

    RenderType1_type = type("RenderType1", (), {"render": RenderType1})
    RenderType2_type = type("RenderType2", (), {"render": RenderType2})
    RenderType3_type = type("RenderType3", (), {"render": RenderType3})

    rule1 = RenderType1_type()
    rule2 = RenderType2_type()
    rule3 = RenderType3_type()

    # Test 1: set new renderfunc
    register.set_renderfunc(RenderType1_type, RenderType3.render)

# Generated at 2022-06-14 08:23:00.420917
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    from .rendertype import Sgr

    class RenderfuncMock:
        def __init__(self, color: str):
            self.color = color

        def __call__(self, *args):
            return self.color

    class RgbRenderfuncMock:
        def __init__(self, color: str):
            self.color = color

        def __call__(self, red, green, blue):
            return self.color

    # Create register and add style-attribute.
    fg = Register()
    fg.red = Style(Sgr(1, 30), Sgr(1))

    # Change Renderfunction
    fg.set_renderfunc(Sgr, RenderfuncMock("\x1b[31m"))

    # Test if style-attribute returns the new string.

# Generated at 2022-06-14 08:23:14.532988
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class _TestRender3(RenderType):
        pass

    class _TestRender4(RenderType):
        pass

    # Test renderfunc
    renderfunc: Callable = lambda *args: "Test3"

    def test_renderfunc(*args, **kwargs):
        return "Test4"

    # Setup
    reg = Register()

    # Before
    assert _TestRender3 not in reg.renderfuncs

    # Test
    reg.set_renderfunc(_TestRender3, renderfunc)

    # After
    assert _TestRender3 in reg.renderfuncs
    assert reg.renderfuncs[_TestRender3] == renderfunc

    # Before
    assert _TestRender4 not in reg.renderfuncs

    # Test
    reg.set_renderfunc(_TestRender4, test_renderfunc)

    # After
    assert _

# Generated at 2022-06-14 08:23:21.998481
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    """
    This unit test checks if we can call set_renderfunc by using an instance of class RenderType.
    """
    from .rendertype import Sgr, RgbFg

    def render_func_1(arg1: int) -> str:
        return "1"

    def render_func_2(arg1: int, arg2: int, arg3: int) -> str:
        return "2"

    reg = Register()

    reg.set_renderfunc(Sgr, render_func_1)
    reg.set_renderfunc(RgbFg, render_func_2)

    assert reg.renderfuncs[Sgr] == render_func_1
    assert reg.renderfuncs[RgbFg] == render_func_2

# Generated at 2022-06-14 08:23:32.216425
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class RgbFg(RenderType):
        pass

    def f1(r, g, b):
        return "rgbfg"

    def f2(x):
        return "x"

    class Hihi(RenderType):
        pass

    def f4(x, y, z):
        return "hihi"

    reg = Register()
    reg.set_renderfunc(RgbFg, f1)
    reg.set_renderfunc(Hihi, f4)
    reg.set_eightbit_call(Hihi)
    assert reg(10, 20, 30) == "hihi"

# Generated at 2022-06-14 08:23:43.450392
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    def func1(x: int) -> str:
        return f"\033[38;5;{x}m"

    def func2(x: int, y: int) -> str:
        return f"\033[{x};{y}m"

    r1 = Register()

    m1 = RenderType("M1", ("x",))
    m2 = RenderType("M2", ("x", "y",))

    r1.set_renderfunc(m1, func1)
    r1.set_renderfunc(m2, func2)

    assert len(r1.renderfuncs) == 2
    assert r1.renderfuncs[m1] == func1
    assert r1.renderfuncs[m2] == func2

# Generated at 2022-06-14 08:23:53.000110
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    """
    Method set_renderfunc is used to add new renderfuns to a register.
    """

    class A(RenderType):
        args = ()

    class B(RenderType):
        args = ()

    def f1(): ...
    def f2(): ...

    r = Register()  # Create a new register-object

    # Add two renderfuncs
    r.set_renderfunc(A, f1)
    r.set_renderfunc(B, f2)

    assert (r.renderfuncs[A] == f1)
    assert (r.renderfuncs[B] == f2)



# Generated at 2022-06-14 08:24:04.018925
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class TestRenderType(RenderType):

        def __init__(self, x, y):
            self.args = (x, y)

    class TestRegister(Register):

        def __init__(self):
            super().__init__()

            self.style = Style(TestRenderType(1, 2))
            self.style2 = Style(TestRenderType(1, 2), TestRenderType(5, 6))
            self.style3 = Style(TestRenderType(1, 2), TestRenderType(5, 6), TestRenderType(8, 9))

    def func(x, y):
        return x, y

    r: TestRegister = TestRegister()

    r.set_renderfunc(TestRenderType, func)

    assert r.style == (1, 2)

# Generated at 2022-06-14 08:24:22.550292
# Unit test for method unmute of class Register
def test_Register_unmute():
    """
    This test sets up a register-object and then mutes it.
    Then it unmutes it.
    """
    fg = Register()
    fg.test = Style(RgbFg(1,2,3))

    fg.mute()
    x: bool = str(fg.test) == ""

    fg.unmute()

    y: bool = str(fg.test) == "\x1b[38;2;1;2;3m"

    assert x and y


# Generated at 2022-06-14 08:24:35.284703
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    """
    Tests the method as_namedtuple of the class register.
    """
    from sty import fg, bg, ef, rs

    fg.red = Style(fg(255, 0, 0))
    fg.green = Style(fg(0, 255, 0))

    register_as_nt: namedtuple = fg.as_namedtuple()

    assert register_as_nt.red == "\033[38;2;255;0;0m"
    assert register_as_nt.green == "\033[38;2;0;255;0m"

# Generated at 2022-06-14 08:24:39.170233
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    import sty
    r = sty.rs.copy()
    for attr in r.__dir__():
        if not attr.startswith("_") and isinstance(r.__getattribute__(attr), str):
            r.__setattr__(attr, "A")
    t = r.as_namedtuple()
    assert t.reset == "A"

# Generated at 2022-06-14 08:24:48.594168
# Unit test for method unmute of class Register
def test_Register_unmute():
    """
    Test if mute and unmute works properly.
    """
    from .register import fg

    # Mute fg
    fg.mute()

    # Test muted state
    assert fg.is_muted == True
    assert fg('red') == ""

    # Unmute fg
    fg.unmute()

    # Test unmuted state
    assert fg.is_muted == False
    assert fg('red') == "\x1b[38;2;255;0;0m"

# Generated at 2022-06-14 08:24:58.026456
# Unit test for method unmute of class Register
def test_Register_unmute():
    """Check if registering a new renderfunc and muted status is working"""
    # Setup
    r = Register()

    class RgbFg(RenderType):
        def __init__(self, r: int, g: int, b: int):
            self.args = (r, g, b)

    def f(r: int, g: int, b: int) -> str:
        return f"\x1b[38;2;{r};{g};{b}m"

    r.set_renderfunc(RgbFg, f)
    r.rgb_call = f
    r.fg = Style(RgbFg(42, 23, 255))
    assert str(r.fg) == "\x1b[38;2;42;23;255m"

    r.mute()

# Generated at 2022-06-14 08:25:03.125850
# Unit test for constructor of class Style
def test_Style():
    style1 = Style(value="123")
    style2 = Style(value="123", rules=["456"])
    style3 = Style(value="123", rules=["456", Style(value="789", rules=["101112"])])
    assert style1 == "123"
    assert style1.rules == tuple()
    assert style2 == "123"
    assert style2.rules == ("456",)
    assert style3 == "123"
    assert style3.rules == ("456", Style("789", rules=("101112",)))

# Generated at 2022-06-14 08:25:08.512211
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    """
    Test the method as_namedtuple of the Register class.
    """
    register = Register()

    register.red = Style(RgbFg(255, 0, 0))
    register.green = Style(RgbFg(0, 255, 0))

    expected_result = RegisterNamedtuple(red="\x1b[38;2;255;0;0m", green="\x1b[38;2;0;255;0m")
    assert register.as_namedtuple() == expected_result



# Generated at 2022-06-14 08:25:11.246835
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    reg = Register()
    reg.a = Style(RenderType())
    reg.b = Style(RenderType())

    assert reg.as_dict() == {'a': '', 'b': ''}



# Generated at 2022-06-14 08:25:20.317796
# Unit test for method copy of class Register
def test_Register_copy():
    import pytest
    from sty import RenderType, fg

    # Create a style object which has an object as an attribute.
    setattr(fg, "my_style", Style(fg(1)))

    before_copy = fg.my_style.rules

    my_fg = fg.copy()
    my_fg.set_renderfunc(RenderType.FGBG, lambda c: f"{c}")

    # Unittest for deepcopy
    assert before_copy == my_fg.my_style.rules

# Generated at 2022-06-14 08:25:23.452176
# Unit test for method unmute of class Register
def test_Register_unmute():
    class St(Register):
        def __init__(self):
            super().__init__()
            self.black = Style()

    st = St()
    st.mute()
    assert st.black == ""
    st.unmute()
    assert st.black != ""

# Generated at 2022-06-14 08:25:38.653519
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    r = Register()
    r.red = Style(RgbFg(255, 0, 0))
    r.blue = Style(RgbFg(0, 0, 255))
    nt = r.as_namedtuple()
    assert nt.red == "\x1b[38;2;255;0;0m"
    assert nt.blue == "\x1b[38;2;0;0;255m"


# Generated at 2022-06-14 08:25:43.556594
# Unit test for constructor of class Style
def test_Style():
    style_str = "\x1b[38;2;1;5;10m\x1b[1m"
    style = Style(RgbFg(1, 5, 10), Sgr(1))

    assert isinstance(style, Style)
    assert str(style) == style_str
    assert isinstance(style, str)



# Generated at 2022-06-14 08:25:46.912296
# Unit test for method copy of class Register
def test_Register_copy():
    # Make a copy of the register object
    r1 = Register()
    r2 = r1.copy()

    # Check if r1 and r2 have the same state
    assert r1.__dict__ == r2.__dict__



# Generated at 2022-06-14 08:25:59.540664
# Unit test for constructor of class Style
def test_Style():

    from .rendertypes import Sgr, RgbFg

    s = Style(Sgr(42, 1), Sgr(43, 2), RgbFg(1, 2, 3), Sgr(44, 3), RgbFg(2, 3, 4))

    assert isinstance(s, Style)
    assert isinstance(s, str)

    assert s.value == "\x1b[42;1m\x1b[43;2m\x1b[38;2;1;2;3m\x1b[44;3m\x1b[38;2;2;3;4m"
    assert s.rules == (Sgr(42, 1), Sgr(43, 2), RgbFg(1, 2, 3), Sgr(44, 3), RgbFg(2, 3, 4))


# Generated at 2022-06-14 08:26:01.183003
# Unit test for method __new__ of class Style
def test_Style___new__():
    style = Style("test")
    assert style == "test"


# Generated at 2022-06-14 08:26:09.750918
# Unit test for method copy of class Register
def test_Register_copy():
    r = Register()

    r.set_renderfunc(str, lambda x: f"{x}")

    r.zero = Style(str("zero"))
    r.one = Style(str("one"))

    r1 = r.copy()

    r.zero = Style(str("two"))

    assert r1.zero == "zero"
    assert r1.one == "one"
    assert r.zero == "two"
    assert r.one == "one"

# Generated at 2022-06-14 08:26:19.161701
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    class RgbFg(RenderType):
        def __init__(self, r, g, b):
            super().__init__((r, g, b))

    def myfunc(r: int, g: int, b: int) -> str:
        template = "\x1b[38;2;{r};{g};{b}m"
        return template.format(r=r, g=g, b=b)

    def myfunc2(r: int, g: int, b: int) -> str:
        template = "\x1b[38;2;{r};{g};{b}m"
        return template.format(r=g, g=b, b=r)

    reg = Register()
    reg.set_renderfunc(RgbFg, myfunc)


# Generated at 2022-06-14 08:26:32.011016
# Unit test for method copy of class Register
def test_Register_copy():

    from .render import Sgr, RgbFg, RgbBg

    r = Register()

    r.set_renderfunc(Sgr, lambda x: f"<SGR-{x}>")

    r.set_renderfunc(RgbFg, lambda *args, **kwargs: f"<RgbFg-{args}-{kwargs}>")

    a = Style(RgbFg(1,2,3), Sgr(5), RgbFg(4,5,6))

    r.test = a

    r1 = r.copy()

    r1.test.rules[1] = Sgr(42)

    assert r.test == Style(RgbFg(1,2,3), Sgr(5), RgbFg(4,5,6))
    assert r.test != Style

# Generated at 2022-06-14 08:26:40.774602
# Unit test for constructor of class Register
def test_Register():
    rendertypes = []
    renderfuncs = {}

    Rendertype = RenderType("Rendertype", rendertypes)
    renderfuncs.update({Rendertype: lambda x: x})

    r = Register()
    r.set_eightbit_call(Rendertype)
    r.set_rgb_call(Rendertype)
    r.set_renderfunc(Rendertype, lambda x, y, z: x)
    r.mute()
    r.unmute()

# Generated at 2022-06-14 08:26:51.761458
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class RenderType_1(RenderType):
        pass

    class RenderType_2(RenderType):
        pass

    func_1: Callable = lambda x: x
    func_2: Callable = lambda x: x

    register_1 = Register()
    register_2 = Register()

    register_1.set_renderfunc(RenderType_1, func_1)
    register_2.set_renderfunc(RenderType_2, func_2)

    register_1.set_eightbit_call(RenderType_1)
    register_2.set_eightbit_call(RenderType_2)

    assert register_1.eightbit_call(4) == func_1(4)

    register_1.set_renderfunc(RenderType_2, func_2)

# Generated at 2022-06-14 08:27:04.631743
# Unit test for method __new__ of class Style
def test_Style___new__():
    """
    Test __new__ of class Style.

    This class exists in order to extend the behavior of str. We have to test
    this because this is a crucial part of the styling concept.
    """

    class TestRenderType(RenderType):
        def __call__(self):
            return "E"

    s = Style(TestRenderType(), value="E")
    assert isinstance(s, str)
    assert str(s) == "E"

# Generated at 2022-06-14 08:27:17.901842
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    from .register import fg, bg, rs, Sgr

    fg.orange = Style(Sgr(1, 38, 5, 255, 100, 0))
    fg.blue = Style(Sgr(1, 38, 5, 0, 0, 255))
    bg.red = Style(Sgr(48, 5, 255, 0, 0))
    rs.reset = Style(Sgr(0))

    assert fg.orange == "\x1b[38;2;255;100;0m\x1b[1m"
    assert fg.blue == "\x1b[38;2;0;0;255m\x1b[1m"
    assert bg.red == "\x1b[48;2;255;0;0m"
    assert rs.reset == "\x1b[0m"

# Generated at 2022-06-14 08:27:29.252648
# Unit test for constructor of class Register
def test_Register():

    def eightbit_render(fg_or_bg, code):
        return f"\x1b[{fg_or_bg};5;{code}m"

    def rgb_render(fg_or_bg, r, g, b):
        return f"\x1b[{fg_or_bg};2;{r};{g};{b}m"

    reg = Register()

    reg.set_renderfunc(RgbFg, rgb_render)
    reg.set_renderfunc(RgbBg, rgb_render)

    reg.set_renderfunc(EightbitFg, eightbit_render)
    reg.set_renderfunc(EightbitBg, eightbit_render)

    reg.purple = Style(RgbFg(10, 0, 200), RgbBg(255, 0, 200))

# Generated at 2022-06-14 08:27:30.709982
# Unit test for constructor of class Register
def test_Register():

    r = Register()
    assert isinstance(r, Register)

# Generated at 2022-06-14 08:27:40.771715
# Unit test for method __new__ of class Style
def test_Style___new__():

    class MyStr(Style):
        pass
        
    mystr = MyStr(value="Hi")
    assert isinstance(mystr, MyStr)
    assert isinstance(mystr, str)
    assert str(mystr) == "Hi"

    mystr = MyStr(value="Hi", rules=[1, 2])
    assert isinstance(mystr, MyStr)
    assert isinstance(mystr, str)
    assert str(mystr) == "Hi"

    mystr = MyStr(value="Hi", rules=[1, 2], other="test")
    assert isinstance(mystr, MyStr)
    assert isinstance(mystr, str)
    assert str(mystr) == "Hi"

    mystr = MyStr(rules=[1, 2])
    assert isinstance(mystr, MyStr)

# Generated at 2022-06-14 08:27:54.124250
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    class TestRenderType(RenderType):
        # fmt: off
        args: List[str]
        renderfunc: Callable

        def __init__(self, *args):
            self.args = self.custom_args(*args)
            self.renderfunc = lambda *args: "Test_PADDING" + "".join(args)
        # fmt: on

        def custom_args(self, *args) -> List[str]:
            return [*args]

    test_register = Register()

    test_register.renderfuncs = {
        TestRenderType: lambda *args: "Test_PADDING" + TestRenderType(*args).renderfunc(*args),
    }

    r1 = TestRenderType("arg1", "arg2")
    r2 = TestRenderType("arg3", "arg4")


# Generated at 2022-06-14 08:28:04.923586
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class TestRegister(Register):
        pass

    r1 = TestRegister()

    class R1(RenderType):
        code = "1"

    class R2(RenderType):
        code = "2"

    r1.set_renderfunc(R1, lambda: f"\x1b[{R1.code}")
    r1.set_renderfunc(R2, lambda: f"\x1b[{R2.code}")

    assert r1.renderfuncs[R1]() == "\x1b[1"
    assert r1.renderfuncs[R2]() == "\x1b[2"



# Generated at 2022-06-14 08:28:15.525345
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    renderfuncs: Renderfuncs = {}
    register = Register()

    for k, v in renderfuncs.items():
        register.set_renderfunc(k, v)

    assert register.eightbit_call(0) == "\x1b[38;5;0m"
    assert register.eightbit_call(123) == "\x1b[38;5;123m"

    assert register.rgb_call(0, 0, 0) == "\x1b[38;2;0;0;0m"
    assert register.rgb_call(255, 128, 32) == "\x1b[38;2;255;128;32m"

    return True



# Generated at 2022-06-14 08:28:17.881464
# Unit test for method copy of class Register
def test_Register_copy():
    """
    Unit test for method copy of class Register.
    """
    # TODO: Implement unit test
    pass

# Generated at 2022-06-14 08:28:22.325746
# Unit test for method unmute of class Register
def test_Register_unmute():
    from .logic import register

    reg = register.fg
    reg.is_muted == False
    reg.mute()
    reg.is_muted == True
    reg.unmute()
    reg.is_muted == False

# Generated at 2022-06-14 08:28:36.927297
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    from sty.ansi import RgbFg, RgbBg

    test_register = Register()
    test_register.set_renderfunc(RgbFg, lambda r, g, b: (r, g, b))

    # Test
    test_register.set_rgb_call(RgbFg)
    assert test_register(0,0,0) == (0, 0, 0)

# Generated at 2022-06-14 08:28:49.646758
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():

    class TestRenderType1(RenderType):
        sgr_code: str  = "999"
        ansi_code: str = "999"
        args: NamedTuple = namedtuple("TestRenderType1Args", ["arg1", "arg2"])("nineninenine", "fivefive")

    class TestRenderType2(RenderType):
        sgr_code: str  = "256"
        ansi_code: str = "256"
        args: NamedTuple = namedtuple("TestRenderType2Args", [])(tuple())

    def func1(*args):
        arg1, arg2 = args
        return f"1: {arg1} / {arg2}"

    def func2():
        return "2: Twotwo"

    r: Register = Register()

# Generated at 2022-06-14 08:28:50.895564
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert isinstance(r, Register)


# Generated at 2022-06-14 08:28:59.364629
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    from sty import fg, bg, ef

    fg.orange = Style(RgbFg(1,5,10))
    fg.red = Style(RgbFg(1,5,10))
    bg.blue = Style(RgbBg(5,5,5))

    print(fg.orange, "orange")
    print(bg.blue, "blue")
    print(ef.bold, "bold")
    print(fg.red, "red")

    x = fg.as_dict()
    assert isinstance(x, dict)
    assert len(x) == 3
    assert x["orange"] == "\x1b[38;2;1;5;10m"
    assert x["red"] == "\x1b[38;2;1;5;10m"


# Unit test

# Generated at 2022-06-14 08:29:09.038438
# Unit test for method __call__ of class Register
def test_Register___call__():

    class Render1(RenderType):
        def ansi_seq_rgb(self, r, g, b):
            return f"Test-Render({r}, {g}, {b})"

    class Render2(RenderType):
        def ansi_seq_8bit(self, n):
            return f"Test-Render({n})"

    reg = Register()
    reg.set_renderfunc(Render1, lambda r, g, b: f"{r}, {g}, {b}")
    reg.set_renderfunc(Render2, lambda n: f"{n}")
    reg.set_rgb_call(Render1)
    reg.set_eightbit_call(Render2)

    assert reg(42) == "42"
    assert reg(11, 22, 33) == "11, 22, 33"
   

# Generated at 2022-06-14 08:29:17.289811
# Unit test for method unmute of class Register
def test_Register_unmute():
    fg = Register()
    fg.red = Style(
        RgbFg(255, 0, 0),
        Sgr(1),
    )

    fg.mute()

    assert fg.red == ""
    assert fg.eightbit_call(42) == ""
    assert fg.rgb_call(0,0,0) == ""

    fg.unmute()

    assert fg.red == "\x1b[38;2;255;0;0m\x1b[1m"
    assert fg.eightbit_call(42) == "\x1b[38;5;42m"
    assert fg.rgb_call(0,0,0) == "\x1b[38;2;0;0;0m"

# Generated at 2022-06-14 08:29:21.268021
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    color_dict = Register().as_dict()
    assert isinstance(color_dict, dict)
    assert len(color_dict) > 0
    assert 'black' in color_dict
    assert color_dict['black'] == '\x1b[30m'


# Generated at 2022-06-14 08:29:23.243742
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert isinstance(r, Register)

# Generated at 2022-06-14 08:29:35.166549
# Unit test for method unmute of class Register
def test_Register_unmute():

    from ..sty import Sty

    sty = Sty()
    fg = sty.reg.fg
    bg = sty.reg.bg

    fg.green = Style(fg.green.rules, value="\x1b[32m")
    bg.red = Style(bg.red.rules, value="\x1b[41m")

    fg.mute()
    bg.mute()

    assert fg.green == ""
    assert bg.red == ""

    fg.unmute()
    bg.unmute()

    assert fg.green == "\x1b[32m"
    assert bg.red == "\x1b[41m"

# Generated at 2022-06-14 08:29:41.951286
# Unit test for method as_dict of class Register
def test_Register_as_dict():

    class MyRegister(Register):
        def __init__(self):
            super().__init__()
            self.red = Style("\x1b[31m")
            self.green = Style("\x1b[32m")

    myreg = MyRegister()
    d = myreg.as_dict()

    assert d == {"red": "\x1b[31m", "green": "\x1b[32m"}


# Generated at 2022-06-14 08:29:51.452377
# Unit test for constructor of class Register
def test_Register():
    assert Register


# Generated at 2022-06-14 08:30:01.181978
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():

    # Setup
    class RgbFg(RenderType):
        ansi = "38"

    class RgbBg(RenderType):
        ansi = "48"

    class Sgr(RenderType):
        ansi = "1"

    class RgbFg255(RenderType):
        ansi = "38;5"


    def render_rgb_fg(r: int, g: int, b: int) -> str:
        return f"\x1b[{RgbFg.ansi};2;{r};{g};{b}m"

    def render_rgb_bg(r: int, g: int, b: int) -> str:
        return f"\x1b[{RgbBg.ansi};2;{r};{g};{b}m"


# Generated at 2022-06-14 08:30:13.443409
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    # Setup test data
    r = Register()
    s = Style(RgbFg(0, 0, 0), Sgr(1))
    rendered_style = Style(RgbFg(0, 0, 0), Sgr(1), value="\x1b[38;2;0;0;0m\x1b[1m")

    # Setup mock callables
    def render_1(r: int, g: int, b: int) -> str:
        return f"\x1b[38;2;{r};{g};{b}m"

    def render_2(arg: int) -> str:
        return f"\x1b[{arg}m"

    r.set_renderfunc(RgbFg, render_1)
    r.set_renderfunc(Sgr, render_2)

# Generated at 2022-06-14 08:30:26.951727
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    """ """
    # Test 1
    class TestRenderType(RenderType):
        def __init__(self):
            RenderType.__init__(self)

    def testfunc(x: int) -> str:
        return x

    reg = Register()

    reg.set_renderfunc(TestRenderType, testfunc)

    assert isinstance(reg.renderfuncs[TestRenderType], type(testfunc))

    # Test 2
    class TestRenderType2(RenderType):
        def __init__(self):
            RenderType.__init__(self)

    def testfunc2(x: int) -> str:
        return x

    reg.set_renderfunc(TestRenderType2, testfunc2)

    assert isinstance(reg.renderfuncs[TestRenderType2], type(testfunc2))



# Generated at 2022-06-14 08:30:28.365273
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    assert Register().as_namedtuple().abc == ""

# Generated at 2022-06-14 08:30:36.831775
# Unit test for method __call__ of class Register
def test_Register___call__():

    class CustomRegister(Register):
        pass

    def eightbit_example_func(x: int) -> str:
        return "8bit_example"

    def rgb_example_func(r: int, g: int, b: int) -> str:
        return "rgb_example"

    r = CustomRegister()
    r.set_eightbit_call(eightbit_example_func)
    r.set_rgb_call(rgb_example_func)
    assert r(8) == "8bit_example"
    assert r(10, 42, 255) == "rgb_example"

# Generated at 2022-06-14 08:30:49.699730
# Unit test for constructor of class Style
def test_Style():
    class Sgr(RenderType):
        def __init__(self, i: int):
            self.args = (i,)
            super().__init__()

        def render(self, i: int) -> str:
            return f"\x1b[{i}m"

        @classmethod
        def reset(cls) -> str:
            return "\x1b[0m"

    def fg(i: int) -> str:
        rgb = (0, 0, 0)
        return Ansi(i, rgb)

    def bg(i: int) -> str:
        rgb = (0, 0, 0)
        return Ansi(i, rgb)

    def ef(i: int) -> str:
        rgb = (0, 0, 0)
        return Ansi(i, rgb)

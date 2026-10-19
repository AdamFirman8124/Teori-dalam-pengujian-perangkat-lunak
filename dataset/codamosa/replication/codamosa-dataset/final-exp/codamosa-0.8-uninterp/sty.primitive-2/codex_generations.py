

# Generated at 2022-06-14 08:20:47.515087
# Unit test for constructor of class Register
def test_Register():

    assert Register()



# Generated at 2022-06-14 08:20:59.228485
# Unit test for method __call__ of class Register
def test_Register___call__():
    # create Register-Object
    rg = Register()

    # populate with some values (without ANSI-sequences)
    rg.a = Style(value="\x1b[42m")
    rg.b = Style(value="\x1b[43m")
    rg.c = Style(value="\x1b[44m")
    rg.d = Style(value="\x1b[45m")
    rg.e = Style(value="\x1b[46m")
    rg.f = Style(value="\x1b[47m")
    rg.g = Style(value="\x1b[48m")
    rg.h = Style(value="\x1b[49m")
    rg.i = Style(value="\x1b[100m")

# Generated at 2022-06-14 08:21:07.586879
# Unit test for method __call__ of class Register
def test_Register___call__():
    r = Register()
    r.renderfuncs.update({
        int: lambda x: "Eightbit-call: " + str(x),
        tuple: lambda r, g, b: "RGB-call: " + str((r, g, b)),
    })

    # Set rendertype for Eightbit-calls.
    r.set_eightbit_call(int)
    assert r(144) == "Eightbit-call: 144"

    # Set rendertype for RGB-calls.
    r.set_rgb_call(tuple)
    assert r(255, 255, 255) == "RGB-call: (255, 255, 255)"

    # Set rendertype for Eightbit-calls.
    r.set_eightbit_call(int)
    assert r(144) == "Eightbit-call: 144"

   

# Generated at 2022-06-14 08:21:11.147466
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert r.is_muted == False

# Generated at 2022-06-14 08:21:15.190465
# Unit test for constructor of class Register
def test_Register():
    reg1 = Register()
    assert reg1.is_muted == False

# Generated at 2022-06-14 08:21:20.385125
# Unit test for method __call__ of class Register
def test_Register___call__():
    r1 = Register()
    r1.set_eightbit_call(RenderType.EIGHTBIT)
    r1.set_rgb_call(RenderType.RGB)
    r1.red = Style("", RenderType.EIGHTBIT("red"))
    assert str(r1("red")) == "red"
    assert r1(1, 2, 3) == (1, 2, 3)



# Generated at 2022-06-14 08:21:22.851150
# Unit test for constructor of class Register
def test_Register():
    register = Register()
    assert isinstance(register, Register)

####################################################################################################

# Unit tests for setter method __setattr__


# Generated at 2022-06-14 08:21:24.153953
# Unit test for constructor of class Register
def test_Register():
    assert Register()



# Generated at 2022-06-14 08:21:33.818634
# Unit test for method __call__ of class Register
def test_Register___call__():
    from .rendertypes import RgbBg

    class R(Register):
        def __init__(self):
            super().__init__()
            setattr(self, "blue", Style(RgbBg(42, 42, 42)))

    r = R()
    r.set_rgb_call(RgbBg)
    r.set_renderfunc(RgbBg, lambda r, g, b: f"\x1b[48;2;{r};{g};{b}m")

    assert r(42, 42, 42) == r.blue


# Generated at 2022-06-14 08:21:34.775932
# Unit test for constructor of class Register
def test_Register():
    pass



# Generated at 2022-06-14 08:21:41.980307
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert r.as_dict() == {}
    assert r.as_namedtuple() == namedtuple('StyleRegister', [])(*[])



# Generated at 2022-06-14 08:21:46.662011
# Unit test for constructor of class Register
def test_Register():

    reg = Register()

    assert len(reg.renderfuncs) == 0

    assert reg.is_muted == False

    assert reg.eightbit_call(0) == 0

    assert reg.rgb_call(0, 0, 0) == (0, 0, 0)

# Generated at 2022-06-14 08:21:55.581028
# Unit test for method __call__ of class Register
def test_Register___call__():

    # Lege ein Register-Objekt an
    rg = Register()

    # Füge einen Farbstil für die Farbe 'red' hinzu
    rg.set_renderfunc(Style, lambda x: "Style:" + x)
    rg.red = Style("red")

    # Setze rendertype für 8Bit-Aufrufe
    rg.set_renderfunc(Eightbit, lambda x: "Eightbit:" + str(x))
    rg.set_eightbit_call(Eightbit)

    # Setze rendertype für RGB-Aufrufe
    rg.set_renderfunc(RgbFg, lambda x, y, z: "Rgb:" + str(x) + "-" + str(y) + "-" + str(z))

# Generated at 2022-06-14 08:21:57.423832
# Unit test for constructor of class Register
def test_Register():

    a = Register()
    b = Register()

    assert a is not b

# Generated at 2022-06-14 08:21:59.328127
# Unit test for constructor of class Register
def test_Register():
    r = Register()
    assert isinstance(r, Register)



# Generated at 2022-06-14 08:22:12.259038
# Unit test for method __call__ of class Register
def test_Register___call__():

    from .rendertype import RgbFg, Sgr

    def render_Sgr(x: int) -> str:
        return f"\x1b[{x}m"

    def render_RgbFg(r: int, g: int, b: int) -> str:
        return f"\x1b[38;2;{r};{g};{b}m"

    def render_RgbBg(r: int, g: int, b: int) -> str:
        return f"\x1b[48;2;{r};{g};{b}m"

    def render_Bold() -> str:
        return "\x1b[1m"

    reg = Register()
    reg.set_renderfunc(Sgr, render_Sgr)

# Generated at 2022-06-14 08:22:21.532549
# Unit test for method __call__ of class Register
def test_Register___call__():
    from sty import fg, bg

    assert fg(42) == '\x1b[38;5;42m'
    assert bg(42) == '\x1b[48;5;42m'
    assert fg('red') == fg.red
    assert bg('red') == bg.red
    assert fg(10, 42, 255) == '\x1b[38;2;10;42;255m'
    assert bg(10, 42, 255) == '\x1b[48;2;10;42;255m'


# Generated at 2022-06-14 08:22:23.073671
# Unit test for constructor of class Register
def test_Register():
    new = Register()
    assert isinstance(new, Register)

# Generated at 2022-06-14 08:22:34.386897
# Unit test for method __call__ of class Register
def test_Register___call__():
    class DummyStyle(Style):
        pass

    class DummyRegister(Register):
        red = DummyStyle("\x1b[1;31m", Sgr(1), Fg(9))
        def __init__(self) -> None:
            self.renderfuncs = {
                Sgr: lambda *_: "\x1b[{:d}m".format(_[0]),
                Fg: lambda *_: "\x1b[38;2;{:d};{:d};{:d}m".format(_[0], _[1], _[2]),
            }
            self.eightbit_call = lambda x: "\x1b[38;5;{:d}m".format(x)

# Generated at 2022-06-14 08:22:45.393271
# Unit test for method __call__ of class Register
def test_Register___call__():

    def test_eightbit(n: int) -> str:
        return f"{n}"

    def test_rgb(r: int, g: int, b: int) -> str:
        return f"{r},{g},{b}"

    r = Register()
    r.set_eightbit_call(lambda x: x)
    r.set_rgb_call(lambda x, y, z: x * y * z)
    r.test_eightbit = Style(test_eightbit)
    r.test_rgb = Style(test_rgb)

    assert r.test_eightbit == "test_eightbit"
    assert r.test_rgb == "test_rgb"

    assert r(10) == "10"
    assert r(10, 42, 255) == "420"

    assert r

# Generated at 2022-06-14 08:22:55.983711
# Unit test for constructor of class Register
def test_Register():
    register = Register()
    assert isinstance(register, Register)

# Generated at 2022-06-14 08:22:57.254005
# Unit test for constructor of class Register
def test_Register():
    # No Args
    Register()



# Generated at 2022-06-14 08:23:06.766460
# Unit test for method __call__ of class Register
def test_Register___call__():

    class DummyRenderType(RenderType):
        pass

    class DummyStyle(str):
        pass

    def render_eightbit(code: int) -> str:
        return str(code)

    def render_rgb(r: int, g: int, b: int) -> str:
        return str(r) + str(g) + str(b)

    class DummyRegister(Register):
        reset: Style

    dummy = DummyRegister()
    dummy.set_renderfunc(DummyRenderType, render_eightbit)
    dummy.reset = Style(DummyRenderType(100))

    assert dummy(100) == "100"
    assert dummy("reset") == dummy.reset
    assert dummy(100, 0, 50) == "100050"

# Generated at 2022-06-14 08:23:18.619934
# Unit test for method __call__ of class Register
def test_Register___call__():
    """
    :return:
    """
    r = Register()
    r.set_renderfunc(RenderType, lambda s: f"{s}")
    r.set_eightbit_call(RenderType)
    r.set_rgb_call(RenderType)

    r.orange = Style(RenderType("orange"), RenderType("bold"))
    r.white = Style(RenderType("white"), RenderType("bold"))

    assert r.orange == "orangebold"
    assert r.white == "whitebold"

    assert r(144) == "144"
    assert r(10, 42, 144) == "10,42,144"
    assert r("orange") == "orangebold"
    assert r("white") == "whitebold"

    # TODO: Add test-cases for mute and unmute.

# Generated at 2022-06-14 08:23:21.456885
# Unit test for constructor of class Register
def test_Register():
    """Unit test for constructor of class Register"""
    reg = Register()
    assert isinstance(reg, Register)

# Generated at 2022-06-14 08:23:25.561816
# Unit test for method __call__ of class Register
def test_Register___call__():
    register = Register()

    register.sample_attribute = "sample_value"

    assert register("sample_attribute") == "sample_value"

    assert register(42) == ""

    assert register(42, 52, 63) == ""

# Generated at 2022-06-14 08:23:26.803062
# Unit test for constructor of class Register
def test_Register():
    register = Register()
    assert register


# Generated at 2022-06-14 08:23:36.642908
# Unit test for constructor of class Register
def test_Register():
    from .rendertype import RgbFg, Sgr

    def test_func(*args, **kwargs):
        return args

    # Let's create a new Register-object and add some Styles.
    new_register = Register()

    # First we have to set the renderfunc for the Sgr-rendertype.
    new_register.set_renderfunc(Sgr, test_func)

    # Then we can add the first Style to our new Register with
    # the keyword 'bold' and the constructor-arguments '1'.
    # We use Sgr(1) as the second argument, because Sgr is already the
    # associated rendertype for the keyword 'fg'.
    new_register.bold = Style(Sgr(1))

    # Next we add a second Style to our new Register.
    # This time we have to set the renderfunc for R

# Generated at 2022-06-14 08:23:38.236711
# Unit test for constructor of class Register
def test_Register():
    assert Register()

# Generated at 2022-06-14 08:23:51.260127
# Unit test for method __call__ of class Register
def test_Register___call__():

    def foo(x: int) -> str:
        return "a"

    def bar(x: int) -> str:
        return "b"

    def baz(r: int, g: int, b: int) -> str:
        return "c"

    def qux(r: int, g: int, b: int) -> str:
        return "d"

    r = Register()
    r.foo = Style()
    r.bar = Style()

    r.set_eightbit_call(None)
    r.set_rgb_call(None)
    r.set_renderfunc(None, foo)
    r.set_renderfunc(None, bar)
    r.set_renderfunc(None, baz)
    r.set_renderfunc(None, qux)


# Generated at 2022-06-14 08:24:20.270513
# Unit test for method __new__ of class Style
def test_Style___new__():
    class Bold(RenderType):
        rendertype = "BOLD"
        default_args = ()

    class BrightWhite(RenderType):
        rendertype = "BRIGHT_WHITE"
        default_args = ()

    s = Style(*(Bold(), BrightWhite()), value="whatever")

    assert s == "whatever"
    assert s.rules == (Bold(), BrightWhite())
    assert type(s) is Style
    assert isinstance(s, str)



# Generated at 2022-06-14 08:24:23.716506
# Unit test for constructor of class Register
def test_Register():
    class TestRegister(Register):
        pass

    tr = TestRegister()
    assert isinstance(tr, TestRegister)
    assert isinstance(tr, Register)



# Generated at 2022-06-14 08:24:36.664466
# Unit test for method mute of class Register
def test_Register_mute():

    class RgbFg(RenderType):

        def __init__(self, r, g, b):
            super().__init__()
            self.args = (r, g, b)

    class RgbBg(RenderType):

        def __init__(self, r, g, b):
            super().__init__()
            self.args = (r, g, b)

    f1 = lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m"
    f2 = lambda r, g, b: f"\x1b[48;2;{r};{g};{b}m"

    reg = Register()
    reg.set_renderfunc(RgbFg, f1)

# Generated at 2022-06-14 08:24:40.916139
# Unit test for constructor of class Register
def test_Register():
    register1 = Register()
    register2 = Register()
    register2.renderfuncs = {int: lambda x: "foo"}
    assert register1.renderfuncs != register2.renderfuncs


# Generated at 2022-06-14 08:24:46.692972
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    r = Register()
    r.foo = "bar"
    r.baz = "bob"
    nt = r.as_namedtuple()
    assert isinstance(nt, NamedTuple)
    assert nt.foo == "bar"
    assert nt.baz == "bob"

# Generated at 2022-06-14 08:24:57.013620
# Unit test for method mute of class Register
def test_Register_mute():
    
    class RgbFg(RenderType): pass
    class RgbBg(RenderType): pass

    new_register = Register()
    new_register.renderfuncs.update({RgbFg: lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m",
                                     RgbBg: lambda r, g, b: f"\x1b[48;2;{r};{g};{b}m"})

    setattr(new_register, "red", Style(RgbFg(255, 0, 0)))
    setattr(new_register, "blue", Style(RgbBg(0, 0, 255)))

# Generated at 2022-06-14 08:25:00.863423
# Unit test for constructor of class Register
def test_Register():

    rg = Register()

    assert isinstance(rg, Register)
    assert rg.as_dict() == {}
    assert rg.as_namedtuple() == namedtuple("StyleRegister", [])()


# Generated at 2022-06-14 08:25:05.729440
# Unit test for constructor of class Register
def test_Register():
    """
    Create a new register and set a couple of attributes.
    """
    # Create Register:
    r = Register()

    # Add attributes:
    for i in range(5):
        setattr(r, str(i), Style(value=str(i)))

    assert len(r.__dict__) == 5, "Wrong number of attributes."



# Generated at 2022-06-14 08:25:07.119960
# Unit test for method unmute of class Register
def test_Register_unmute():
    assert True, "TODO"


# Generated at 2022-06-14 08:25:11.788897
# Unit test for method __call__ of class Register
def test_Register___call__():

    class TestRegister(Register):
        def __init__(self):
            super().__init__()
            self.set_renderfunc(RenderType, lambda x: x)

    tr = TestRegister()

    assert tr(42) == 42
    assert tr("str") == "str"
    assert tr(1, 2, 3) == (1, 2, 3)

# Generated at 2022-06-14 08:25:59.638090
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    import sty

    # Create test register.
    register = sty.register(
        custom_fg=[(12, 12, 12), (13, 13, 13), (14, 14, 14), (15, 15, 15)],
    )

    # Export register as namedtuple
    T = register.as_namedtuple()

    assert isinstance(T, namedtuple)
    assert T.custom_fg_0 == "\x1b[38;2;12;12;12m"
    assert T.custom_fg_1 == "\x1b[38;2;13;13;13m"
    assert T.custom_fg_2 == "\x1b[38;2;14;14;14m"
    assert T.custom_fg_3 == "\x1b[38;2;15;15;15m"

# Generated at 2022-06-14 08:26:07.436880
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    from .rendertype import RgbBg, RgbFg

    renderfuncs: Renderfuncs = {RgbBg: lambda r, g, b: "\x1b[48;2;{};{};{}m".format(r, g, b)}

    reg = Register()
    reg.set_renderfunc(RgbFg, lambda r, g, b: "\x1b[38;2;{};{};{}m".format(r, g, b))

    assert reg.renderfuncs == {RgbFg: lambda r, g, b: "\x1b[38;2;{};{};{}m".format(r, g, b)}


# Generated at 2022-06-14 08:26:18.332604
# Unit test for constructor of class Register
def test_Register():

    from .rendertype import EightBit, RgbFg, Sgr

    new_register = Register()

    new_register.set_renderfunc(EightBit, lambda x: "")
    new_register.set_renderfunc(RgbFg, lambda r, g, b: "")
    new_register.set_renderfunc(Sgr, lambda x: "")

    new_register.set_eightbit_call(EightBit)
    new_register.set_rgb_call(RgbFg)

    new_register.red = Style(EightBit(1), RgbFg(2, 3, 4))

    # Check if fg is function
    assert callable(new_register)

    # Call fg with an integer as argument
    new_register(1)

    # Call fg with a stribg as argument


# Generated at 2022-06-14 08:26:31.693854
# Unit test for method unmute of class Register
def test_Register_unmute():
    from .rendertype import Eightbit, RgbFg, RgbBg, Sgr, Efg

    # Create a new register
    reg = Register()

    # Set renderfuncs for Sgr and RgbFg
    reg.set_renderfunc(Sgr, lambda *args: f"\x1b[{args[0]}m")
    reg.set_renderfunc(RgbFg, lambda *args: f"\x1b[38;2;{args[0]};{args[1]};{args[2]}m")

    # Create some styles
    fg = Style(RgbFg(10, 20, 30))
    bg = Style(Sgr(2), RgbBg(40, 50, 60))
    ef = Style(Efg(70, 80, 90, 100, 110, 120))

# Generated at 2022-06-14 08:26:37.891577
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    r = Register()
    setattr(r, "name", Style(RgbFg(10, 20, 30), Sgr(1)))
    assert r.as_dict() == {"name": "\x1b[38;2;10;20;30m\x1b[1m"}


# Generated at 2022-06-14 08:26:43.150888
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():

    class RegisterMock(Register):
        def __init__(self):
            super().__init__()
            self.renderfuncs[RenderType] = lambda: ""

    reg = RegisterMock()
    reg.test = Style(RenderType())

    assert isinstance(reg.test, Style)

# Generated at 2022-06-14 08:26:52.706758
# Unit test for method __call__ of class Register
def test_Register___call__():

    from .rendertype import Eightbit, RgbFg, Sgr

    r = Register()

    # Set up register.
    r.reset = Style(Sgr(0))
    r.red = Style(Eightbit(1))
    r.rgb_red = Style(RgbFg(255, 0, 0))

    # Set the renderfunctions
    r.set_renderfunc(Eightbit, lambda a: "<EIGHTBIT>" + str(a))
    r.set_renderfunc(RgbFg, lambda r, g, b: "<RGB>" + str(r) + str(g) + str(b))

    # Set the calls.
    r.set_eightbit_call(Eightbit)
    r.set_rgb_call(RgbFg)

    # Test Eightbit call.

# Generated at 2022-06-14 08:27:04.814951
# Unit test for constructor of class Style
def test_Style():

    class RgbFg(RenderType):
        def __init__(self, r, g, b):
            self.r, self.g, self.b = r, g, b

        @staticmethod
        def render(*args):
            r, g, b = args
            return f"\x1b[38;2;{r};{g};{b}m"


    class Sgr(RenderType):
        def __init__(self, code):
            self.code = code

        @staticmethod
        def render(*args):
            code = args[0]
            return f"\x1b[{code}m"


    class RgbBg(RenderType):
        def __init__(self, r, g, b):
            self.r, self.g, self.b = r, g, b

# Generated at 2022-06-14 08:27:18.005589
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    class NewRegister(Register):
        def __init__(self):
            super().__init__()

            self.red = Style(RgbFg(255, 0, 0))
            self.green = Style(RgbFg(0, 255, 0))
            self.blue = Style(RgbFg(0, 0, 255))

            def _render(r: int, g: int, b: int) -> str:
                return "R{r}G{g}B{b}".format(r=r, g=g, b=b)

            self.set_renderfunc(RgbFg, _render)

    register = NewRegister()


# Generated at 2022-06-14 08:27:20.651238
# Unit test for constructor of class Style
def test_Style():
    s1 = Style(value="hello")
    assert s1 == "hello"

    s2 = Style(value="world")
    assert s2 == "world"



# Generated at 2022-06-14 08:28:59.299880
# Unit test for method copy of class Register
def test_Register_copy():
    r1 = Register()
    r1.test = Style(None)
    r1.test2 = Style('test')
    r2 = r1.copy()
    assert r1.test == r2.test
    assert r1.test2 == r2.test2
    assert r1.test is not r2.test
    assert r1.test2 is not r2.test2

# Generated at 2022-06-14 08:29:05.130115
# Unit test for method copy of class Register
def test_Register_copy():
    reg = Register()
    reg.red = Style(RgbFg(10, 10, 10))
    copy = reg.copy()
    assert copy.red == reg.red

    copy.red = Style(Bold())
    assert copy.red != reg.red

    reg.green = Style(Bold())
    assert hasattr(copy, "green") is False



# Generated at 2022-06-14 08:29:18.866476
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    """
    Unit test for method as_dict of class Register.
    """
    _8bit_call = lambda x: str(x)
    _rgb_call = lambda r, g, b: f"{r}.{g}.{b}"

    r = Register()
    r.set_eightbit_call(_8bit_call)
    r.set_rgb_call(_rgb_call)
    setattr(r, "test_8bit_call", Style(1))
    setattr(r, "test_rgb_call", Style(1, 2, 3))
    setattr(r, "test_nested_call", Style(Style(1)))


# Generated at 2022-06-14 08:29:24.155018
# Unit test for method copy of class Register
def test_Register_copy():
    import random

    random.seed(0)
    r1 = Register()
    r2 = r1.copy()

    assert r1 is not r2

    attrs1 = dir(r1)
    attrs2 = dir(r2)

    assert attrs1 == attrs2

    for attr_name in attrs1:
        if attr_name.startswith("_"):
            continue
        attr1 = getattr(r1, attr_name)
        attr2 = getattr(r1, attr_name)

        assert attr1 == attr2
        assert attr1 is not attr2

    assert random.randint(0, 1000)

# Generated at 2022-06-14 08:29:36.514963
# Unit test for method __call__ of class Register
def test_Register___call__():

    # Test Eightbit-call with rendertype Eightbit.
    r1 = Register()
    r1.set_eightbit_call(Eightbit)
    assert r1(144) == "\u001b[38;5;144m"

    # Test RGB-call with rendertype Rgb.
    r1 = Register()
    r1.set_rgb_call(Rgb)
    assert r1(20, 30, 40) == "\u001b[38;2;20;30;40m"

    # Test 'named-call' with rendertype namedtuple.
    r1 = Register()
    r1.test = "Test"
    assert r1("test") == "Test"


# Generated at 2022-06-14 08:29:48.654136
# Unit test for method mute of class Register
def test_Register_mute():

    from .sty import fg
    from .sty import sgr, RgbFg
    from .sty import RgbBg, Ef
    from .sty import SGR_RESET

    fg.orange = Style(
        RgbFg(255, 128, 0),
        sgr.bold,
        sgr.underline,
    )

    fg.orange_bg = Style(
        RgbBg(255, 128, 0),
        sgr.bold,
        sgr.underline,
    )

    A = fg.orange
    B = fg.orange_bg

    # Test before muting
    assert A == "\x1b[38;2;255;128;0m\x1b[1m\x1b[4m"

# Generated at 2022-06-14 08:29:49.426750
# Unit test for method __call__ of class Register
def test_Register___call__():
    pass

# Generated at 2022-06-14 08:29:59.925384
# Unit test for method __call__ of class Register
def test_Register___call__():

    r1 = Register()

    class RC1(RenderType):
        def __init__(self, x):
            self.args = [x]
    
    class RC2(RenderType):
        def __init__(self, x, y, z):
            self.args = [x, y, z]
    
    def c1(x):
        return str(x)

    def c2(x, y, z):
        return str(x + y + z)

    # registerfunc
    r1.set_renderfunc(RC1, c1)
    r1.set_renderfunc(RC2, c2)

    # eightbitcall
    r1.set_eightbit_call(RC1)

    # rgbcall
    r1.set_rgb_call(RC2)

    # Styles
   

# Generated at 2022-06-14 08:30:07.341970
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    from .rendertype import Sgr

    r1 = Register()
    r1.set_renderfunc(Sgr, lambda x: f"\x1b[{x}m")

    r1.bold = Style(Sgr(1))

    assert str(r1.bold) == "\x1b[1m"

    r1.bold = Style(Sgr(3))

    assert str(r1.bold) == "\x1b[3m"



# Generated at 2022-06-14 08:30:19.189959
# Unit test for method as_dict of class Register
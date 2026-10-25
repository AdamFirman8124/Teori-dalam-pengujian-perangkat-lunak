

# Generated at 2026-10-25 01:19:08.554589
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:19:10.970120
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:19:13.384691
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:19:15.802727
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-25 01:19:17.204348
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    from sty.register import Register, Style
    from sty.rendertype import RgbFg

    reg = Register()
    reg.set_renderfunc(RgbFg, lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m")
    reg.red = Style(RgbFg(255, 0, 0))
    reg.blue = Style(RgbFg(0, 0, 255))

    nt = reg.as_namedtuple()

    assert isinstance(nt, tuple)
    assert nt.red == "\x1b[38;2;255;0;0m"
    assert nt.blue == "\x1b[38;2;0;0;255m"
    assert set(nt._fields) == set(reg.as_dict().keys())
    assert nt.red == reg.as_dict()["red"]
    assert tuple(nt) == tuple(reg.as_dict().values())

# Generated at 2026-10-25 01:19:18.526915
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():
    from sty.register import Register, Style
    from sty.rendertype import RgbFg

    reg = Register()
    reg.set_renderfunc(RgbFg, lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m")
    reg.red = Style(RgbFg(255, 0, 0))
    reg.blue = Style(RgbFg(0, 0, 255))

    nt = reg.as_namedtuple()

    assert isinstance(nt, tuple)
    assert nt.red == "\x1b[38;2;255;0;0m"
    assert nt.blue == "\x1b[38;2;0;0;255m"
    assert set(nt._fields) == set(reg.as_dict().keys())
    assert nt.red == reg.as_dict()["red"]
    assert tuple(nt) == tuple(reg.as_dict().values())

# Generated at 2026-10-25 01:19:27.987422
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class DummyRenderType(RenderType):
        pass

    register = Register()

    register.set_renderfunc(DummyRenderType, lambda value: f"<{value}>")
    register.example = Style(DummyRenderType(42))

    assert register.renderfuncs[DummyRenderType](42) == "<42>"
    assert register.example == "<42>"

    # Replacing the render function should re-render existing styles.
    replacement = lambda value: f"[{value}]"
    register.set_renderfunc(DummyRenderType, replacement)

    assert register.renderfuncs[DummyRenderType] is replacement
    assert register.example == "[42]"
    assert len(tuple(register.example.rules)) == 1
    assert isinstance(tuple(register.example.rules)[0], DummyRenderType)

# Generated at 2026-10-25 01:19:29.316105
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():from sty.register import Register, Style

# Generated at 2026-10-25 01:19:55.324613
# Unit test for method as_dict of class Register
def test_Register_as_dict():register = Register()

# Generated at 2026-10-25 01:19:57.742690
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:20:00.157411
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:20:02.572388
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:20:04.987468
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:20:07.401609
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:20:09.818744
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:20:12.232822
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:20:14.648068
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:20:17.065821
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:20:19.480222
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:20:21.896642
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:20:23.279670
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():from sty.register import Register, Style

# Generated at 2026-10-25 01:20:24.610754
# Unit test for method mute of class Register
def test_Register_mute():
    r = Register()
    r.set_renderfunc(DummyRenderType, lambda x: f"\x1b[{x}m")
    r.red = Style(DummyRenderType("31"))

    # Sanity check: unmuted register renders the ANSI sequence.
    assert str(r.red) == "\x1b[31m"

    r.mute()

    # 1. Mute flag is set.
    assert r.is_muted is True

    # 2. All Style attributes are re-rendered to empty strings,
    #    but their rules are preserved for unmute.
    assert str(r.red) == ""
    assert r.red.rules == (DummyRenderType("31"),)

    # 3. Direct calls return "" while muted.
    assert r("red") == ""

    # 4. New attributes assigned while muted are also blanked.
    r.blue = Style(DummyRenderType("34"))
    assert str(r.blue) == ""

    # 5. Unmute restores everything from the saved rules.
    r.unmute()
    assert r.is_muted is False
    assert str(r.red) == "\x1b[31m"
    assert str(r.blue) == "\x1b[34m"

# Generated at 2026-10-25 01:20:25.937109
# Unit test for method mute of class Register
def test_Register_mute():
    from sty import Register, Style
    from sty.rendertype import RenderType

    class Dummy(RenderType):
        def __init__(self, code: int):
            self.args = (code,)

    r = Register()
    r.renderfuncs[Dummy] = lambda code: f"<{code}>"
    r.eightbit_call = lambda x: f"8bit({x})"
    r.rgb_call = lambda red, green, blue: f"rgb({red},{green},{blue})"

    r.red = Style(Dummy(31))
    assert str(r.red) == "<31>"
    assert r("red") == "<31>"

    r.mute()
    assert r.is_muted is True
    assert str(r.red) == ""
    assert r("red") == ""
    assert r(42) == ""
    assert r(1, 2, 3) == ""
    assert len(r.red.rules) == 1
    assert isinstance(r.red.rules[0], Dummy)
    assert r.red.rules[0].args == (31,)

    r.unmute()
    assert r.is_muted is False
    assert str(r.red) == "<31>"
    assert r("red") == "<31>"
    assert r(42) == "8bit(42)"
    assert r(1, 2, 3) == "rgb(1,2,3)"

# Generated at 2026-10-25 01:20:27.266913
# Unit test for method mute of class Register
def test_Register_mute():
    from sty import Register, Style
    from sty.rendertype import RenderType

    class Dummy(RenderType):
        def __init__(self, code: int):
            self.args = (code,)

    r = Register()
    r.renderfuncs[Dummy] = lambda code: f"<{code}>"
    r.eightbit_call = lambda x: f"8bit({x})"
    r.rgb_call = lambda red, green, blue: f"rgb({red},{green},{blue})"

    r.red = Style(Dummy(31))
    assert str(r.red) == "<31>"
    assert r("red") == "<31>"

    r.mute()
    assert r.is_muted is True
    assert str(r.red) == ""
    assert r("red") == ""
    assert r(42) == ""
    assert r(1, 2, 3) == ""
    assert len(r.red.rules) == 1
    assert isinstance(r.red.rules[0], Dummy)
    assert r.red.rules[0].args == (31,)

    r.unmute()
    assert r.is_muted is False
    assert str(r.red) == "<31>"
    assert r("red") == "<31>"
    assert r(42) == "8bit(42)"
    assert r(1, 2, 3) == "rgb(1,2,3)"

# Generated at 2026-10-25 01:20:37.412323
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class DummyRenderType(RenderType):
        pass

    register = Register()

    initial_renderfunc = lambda value: f"<{value}>"
    register.set_renderfunc(DummyRenderType, initial_renderfunc)

    # The render function is registered and used for newly assigned styles.
    assert register.renderfuncs[DummyRenderType] is initial_renderfunc

    register.example = Style(DummyRenderType(42))
    assert register.example == "<42>"

    # Replacing the function re-renders existing Style attributes.
    replacement_renderfunc = lambda value: f"[{value}]"
    register.set_renderfunc(DummyRenderType, replacement_renderfunc)

    assert register.renderfuncs[DummyRenderType] is replacement_renderfunc
    assert register.example == "[42]"
    assert isinstance(register.example, Style)
    assert len(tuple(register.example.rules)) == 1
    assert isinstance(tuple(register.example.rules)[0], DummyRenderType)

# Generated at 2026-10-25 01:20:38.745186
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():from sty.register import Register, Style

# Generated at 2026-10-25 01:20:52.975577
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class TestRenderType(RenderType):
        pass

    register = Register()
    rule = TestRenderType(42)

    register.set_renderfunc(TestRenderType, lambda value: f"old:{value}")
    register.example = Style(rule)

    assert register.example == "old:42"

    def new_renderfunc(value: int) -> str:
        return f"new:{value}"

    register.set_renderfunc(TestRenderType, new_renderfunc)

    assert register.renderfuncs[TestRenderType] is new_renderfunc
    assert register.example == "new:42"
    assert register.example.rules == (rule,)

# Generated at 2026-10-25 01:20:54.304209
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():from sty.register import Register, Style

# Generated at 2026-10-25 01:20:55.739985
# Unit test for constructor of class Register
def test_Register():
    reg = Register()

    assert reg.renderfuncs == {}
    assert isinstance(reg.renderfuncs, dict)
    assert reg.is_muted is False

    assert callable(reg.eightbit_call)
    assert reg.eightbit_call(42) == 42
    assert reg.eightbit_call("red") == "red"

    assert callable(reg.rgb_call)
    assert reg.rgb_call(10, 20, 30) == (10, 20, 30)

    other = Register()
    reg.renderfuncs[object] = lambda x: x  # type: ignore
    reg.is_muted = True
    assert other.renderfuncs == {}
    assert other.is_muted is False

# Generated at 2026-10-25 01:20:58.406397
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:21:00.939326
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:21:03.471903
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:21:05.888133
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:21:08.303115
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:21:10.719937
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:21:13.133988
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:21:15.549167
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:21:17.963900
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:21:20.378513
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:21:22.794004
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:21:25.208633
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:21:27.623955
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:21:30.039858
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:21:32.456058
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:21:49.218354
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class TestRenderType(RenderType):
        pass

    register = Register()

    register.set_renderfunc(TestRenderType, lambda value: f"old:{value}")
    register.example = Style(TestRenderType(42))

    assert register.example == "old:42"

    def new_renderfunc(value: int) -> str:
        return f"new:{value}"

    register.set_renderfunc(TestRenderType, new_renderfunc)

    # The render function is replaced in the registry.
    assert register.renderfuncs[TestRenderType] is new_renderfunc

    # Existing Style attributes are re-rendered with the new function.
    assert isinstance(register.example, Style)
    assert register.example == "new:42"
    assert len(tuple(register.example.rules)) == 1
    assert isinstance(tuple(register.example.rules)[0], TestRenderType)

# Generated at 2026-10-25 01:21:50.630206
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():from sty.register import Register, Style

# Generated at 2026-10-25 01:22:16.331425
# Unit test for method unmute of class Register
def test_Register_unmute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(
        DummyRenderType,
        lambda value: f"<{value}>",
    )
    register.accent = Style(DummyRenderType("accent"))

    assert register.accent == "<accent>"

    register.mute()
    assert register.is_muted is True
    assert register.accent == ""

    register.unmute()
    assert register.is_muted is False
    assert register.ac

# Generated at 2026-10-25 01:22:32.816650
# Unit test for method unmute of class Register
def test_Register_unmute():
    from sty import Register, Style
    from sty.rendertype import Sgr

    r = Register()
    r.set_renderfunc(Sgr, lambda num: f"<sgr-{num}>")
    r.accent = Style(Sgr(1), Sgr(4))

    # Sanity check: unmuted register renders the style.
    assert r.accent == "<sgr-1><sgr-4>"

    # Mute: all styles must render as empty strings.
    r.mute()
    assert r.is_muted is True
    assert r.accent == ""

    # Unmute: styles must be rendered again with the same rules.
    r.unmute()
    assert r.is_muted is False
    assert r.accent == "<sgr-1><sgr-4>"

    # New assignments after unmuting must render normally too.
    r.bold = Style(Sgr(1))
    assert r.bold == "<sgr-1>"

# Generated at 2026-10-25 01:22:44.797122
# Unit test for method unmute of class Register
def test_Register_unmute():register = Register()
register.mute()
result = register.unmute()

assert result is None
assert register.is_muted is False

# Generated at 2026-10-25 01:22:46.231341
# Unit test for method mute of class Register
def test_Register_mute():
    r = Register()
    r.set_renderfunc(DummyRenderType, lambda x: f"\x1b[{x}m")
    r.red = Style(DummyRenderType("31"))

    # Sanity check: unmuted register renders the ANSI sequence.
    assert str(r.red) == "\x1b[31m"

    r.mute()

    # 1. Mute flag is set.
    assert r.is_muted is True

    # 2. All Style attributes are re-rendered to empty strings,
    #    but their rules are preserved for unmute.
    assert str(r.red) == ""
    assert r.red.rules == (DummyRenderType("31"),)

    # 3. Direct calls return "" while muted.
    assert r("red") == ""

    # 4. New attributes assigned while muted are also blanked.
    r.blue = Style(DummyRenderType("34"))
    assert str(r.blue) == ""

    # 5. Unmute restores everything from the saved rules.
    r.unmute()
    assert r.is_muted is False
    assert str(r.red) == "\x1b[31m"
    assert str(r.blue) == "\x1b[34m"

# Generated at 2026-10-25 01:22:47.664839
# Unit test for method mute of class Register
def test_Register_mute():
    from sty import Register, Style
    from sty.rendertype import RenderType

    class Dummy(RenderType):
        def __init__(self, code: int):
            self.args = (code,)

    r = Register()
    r.renderfuncs[Dummy] = lambda code: f"<{code}>"
    r.eightbit_call = lambda x: f"8bit({x})"
    r.rgb_call = lambda red, green, blue: f"rgb({red},{green},{blue})"

    r.red = Style(Dummy(31))
    assert str(r.red) == "<31>"
    assert r("red") == "<31>"

    r.mute()
    assert r.is_muted is True
    assert str(r.red) == ""
    assert r("red") == ""
    assert r(42) == ""
    assert r(1, 2, 3) == ""
    assert len(r.red.rules) == 1
    assert isinstance(r.red.rules[0], Dummy)
    assert r.red.rules[0].args == (31,)

    r.unmute()
    assert r.is_muted is False
    assert str(r.red) == "<31>"
    assert r("red") == "<31>"
    assert r(42) == "8bit(42)"
    assert r(1, 2, 3) == "rgb(1,2,3)"

# Generated at 2026-10-25 01:22:48.999690
# Unit test for method mute of class Register
def test_Register_mute():
    from sty import Register, Style
    from sty.rendertype import RenderType

    class Dummy(RenderType):
        def __init__(self, code: int):
            self.args = (code,)

    r = Register()
    r.renderfuncs[Dummy] = lambda code: f"<{code}>"
    r.eightbit_call = lambda x: f"8bit({x})"
    r.rgb_call = lambda red, green, blue: f"rgb({red},{green},{blue})"

    r.red = Style(Dummy(31))
    assert str(r.red) == "<31>"
    assert r("red") == "<31>"

    r.mute()
    assert r.is_muted is True
    assert str(r.red) == ""
    assert r("red") == ""
    assert r(42) == ""
    assert r(1, 2, 3) == ""
    assert len(r.red.rules) == 1
    assert isinstance(r.red.rules[0], Dummy)
    assert r.red.rules[0].args == (31,)

    r.unmute()
    assert r.is_muted is False
    assert str(r.red) == "<31>"
    assert r("red") == "<31>"
    assert r(42) == "8bit(42)"
    assert r(1, 2, 3) == "rgb(1,2,3)"

# Generated at 2026-10-25 01:22:50.429396
# Unit test for method mute of class Register
def test_Register_mute():
    r = Register()
    r.set_renderfunc(DummyRenderType, lambda x: f"\x1b[{x}m")
    r.red = Style(DummyRenderType("31"))

    # Sanity check: unmuted register renders the ANSI sequence.
    assert str(r.red) == "\x1b[31m"

    r.mute()

    # 1. Mute flag is set.
    assert r.is_muted is True

    # 2. All Style attributes are re-rendered to empty strings,
    #    but their rules are preserved for unmute.
    assert str(r.red) == ""
    assert r.red.rules == (DummyRenderType("31"),)

    # 3. Direct calls return "" while muted.
    assert r("red") == ""

    # 4. New attributes assigned while muted are also blanked.
    r.blue = Style(DummyRenderType("34"))
    assert str(r.blue) == ""

    # 5. Unmute restores everything from the saved rules.
    r.unmute()
    assert r.is_muted is False
    assert str(r.red) == "\x1b[31m"
    assert str(r.blue) == "\x1b[34m"

# Generated at 2026-10-25 01:22:51.863775
# Unit test for method mute of class Register
def test_Register_mute():
    from sty import Register, Style
    from sty.rendertype import RenderType

    class Dummy(RenderType):
        def __init__(self, code: int):
            self.args = (code,)

    r = Register()
    r.renderfuncs[Dummy] = lambda code: f"<{code}>"
    r.eightbit_call = lambda x: f"8bit({x})"
    r.rgb_call = lambda red, green, blue: f"rgb({red},{green},{blue})"

    r.red = Style(Dummy(31))
    assert str(r.red) == "<31>"
    assert r("red") == "<31>"

    r.mute()
    assert r.is_muted is True
    assert str(r.red) == ""
    assert r("red") == ""
    assert r(42) == ""
    assert r(1, 2, 3) == ""
    assert len(r.red.rules) == 1
    assert isinstance(r.red.rules[0], Dummy)
    assert r.red.rules[0].args == (31,)

    r.unmute()
    assert r.is_muted is False
    assert str(r.red) == "<31>"
    assert r("red") == "<31>"
    assert r(42) == "8bit(42)"
    assert r(1, 2, 3) == "rgb(1,2,3)"

# Generated at 2026-10-25 01:22:53.298020
# Unit test for method mute of class Register
def test_Register_mute():
    from sty import Register, Style
    from sty.rendertype import RenderType

    class Dummy(RenderType):
        def __init__(self, code: int):
            self.args = (code,)

    r = Register()
    r.renderfuncs[Dummy] = lambda code: f"<{code}>"
    r.eightbit_call = lambda x: f"8bit({x})"
    r.rgb_call = lambda red, green, blue: f"rgb({red},{green},{blue})"

    r.red = Style(Dummy(31))
    assert str(r.red) == "<31>"
    assert r("red") == "<31>"

    r.mute()
    assert r.is_muted is True
    assert str(r.red) == ""
    assert r("red") == ""
    assert r(42) == ""
    assert r(1, 2, 3) == ""
    assert len(r.red.rules) == 1
    assert isinstance(r.red.rules[0], Dummy)
    assert r.red.rules[0].args == (31,)

    r.unmute()
    assert r.is_muted is False
    assert str(r.red) == "<31>"
    assert r("red") == "<31>"
    assert r(42) == "8bit(42)"
    assert r(1, 2, 3) == "rgb(1,2,3)"

# Generated at 2026-10-25 01:23:08.657182
# Unit test for method unmute of class Register
def test_Register_unmute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(
        DummyRenderType,
        lambda value: f"<{value}>",
    )

    register.mute()
    register.example = Style(DummyRenderType("example"))

    assert register.is_muted is True
    assert register.example == ""

    register.unmute()

    assert register.is_muted is False
    assert register.example == "<example>"
    assert isinstance(register.example, Style)
    assert register.example.rules == (DummyRenderType("example"),)

# Generated at 2026-10-25 01:23:47.922607
# Unit test for method unmute of class Register
def test_Register_unmute():register = Register()

class _DummyRenderType(RenderType):
    pass

register.renderfuncs[_DummyRenderType] = lambda *args: "\x1b[31m"
register.red = Style(_DummyRenderType((31,)), value="\x1b[31m")

assert str(register.red) == "\x1b[31m"

register.mute()
assert register.is_muted is True
assert str(register.red) == ""

register.unmute()
assert register.is_muted is False
assert str(register.red) == "\x1b[31m"

# Generated at 2026-10-25 01:24:09.413623
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class TestRenderType(RenderType):
        def __init__(self, *args):
            self.args = args

    register = Register()

    def initial_renderer(*args):
        return f"initial:{','.join(map(str, args))}"

    register.set_renderfunc(TestRenderType, initial_renderer)

    assert register.renderfuncs[TestRenderType] is initial_renderer

    rule = TestRenderType(1, 2, 3)
    register.example = Style(rule)

    assert register.example == "initial:1,2,3"
    assert tuple(register.example.rules) == (rule,)

    def replacement_renderer(*args):
        return f"replacement:{'-'.join(map(str, args))}"

    register.set_renderfunc(TestRenderType, replacement_renderer)

    # The render function is replaced and existing Style attributes are rerendered.
    assert register.renderfuncs[TestRenderType] is replacement_renderer
    assert register.example == "replacement:1-2-3"
    assert tuple(register.example.rules) == (rule,)

# Generated at 2026-10-25 01:24:24.753686
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class ExampleRenderType(RenderType):
        pass

    register = Register()
    rule = ExampleRenderType(1, 2, 3)

    # Set up an existing style using the original render function.
    register.renderfuncs[ExampleRenderType] = (
        lambda *args: f"old({','.join(map(str, args))})"
    )
    register.example = Style(rule)

    assert register.example == "old(1,2,3)"

    # Replacing the render function should also rerender existing styles.
    def new_renderfunc(*args):
        return f"new({','.join(map(str, args))})"

    register.set_renderfunc(ExampleRenderType, new_renderfunc)

    assert register.renderfuncs[ExampleRenderType] is new_renderfunc
    assert isinstance(register.example, Style)
    assert register.example == "new(1,2,3)"
    assert tuple(register.example.rules) == (rule,)

# Generated at 2026-10-25 01:24:27.171670
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:24:29.586630
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:24:32.113014
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:24:34.527569
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:24:36.941872
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:24:39.356534
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:24:41.779005
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:24:44.200942
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:24:46.606951
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:24:49.021401
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:24:51.439043
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:24:53.855274
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:24:56.270362
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:24:58.684719
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:25:01.099548
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:25:03.515038
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:25:05.931281
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:25:20.467169
# Unit test for method unmute of class Register
def test_Register_unmute():
    class TestRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(
        TestRenderType,
        lambda value: f"<rendered:{value}>",
    )

    rule = TestRenderType("value")
    register.example = Style(rule)

    assert register.example == "<rendered:value>"

    register.mute()
    assert register.is_muted is True
    assert register.example == ""
    assert register.example.rules == (rule,)

    register.unmute()

    assert register.is_muted is False
    assert isinstance(register.example, Style)
    assert register.example == "<rendered:value>"
    assert register.example.rules == (rule,)

# Generated at 2026-10-25 01:25:43.703589
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:25:46.121411
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:25:48.643917
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:25:51.167217
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:25:53.582902
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:25:55.997914
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:25:58.411913
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:26:00.932483
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:26:03.454293
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:26:05.869153
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:26:08.284783
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:26:22.694616
# Unit test for method mute of class Register
def test_Register_mute():
    # Setup: create a register with a working render function and one style attribute.
    register = Register()
    register.set_renderfunc(RenderType, lambda *args: "\x1b[31m")

    register.red = Style(RenderType("red"))

    # Sanity check: rendering works before muting.
    assert register.is_muted is False
    assert str(register.red) == "\x1b[31m"
    assert register("red") == str(register.red)

    # Mute: all style attributes must render as empty strings.
    register.mute()
    assert register.is_muted is True
    assert str(register.red) == ""
    assert register("red") == ""

    # Calls with 8bit and RGB codes must also return empty strings while muted.
    assert register(42) == ""
    assert register(10, 20, 30) == ""

    # The original styling rules must be preserved (so unmute can restore them).
    assert len(register.red.rules) == 1
    assert isinstance(register.red.rules[0], RenderType)

    # New attributes assigned while muted must also render as empty strings.
    register.blue = Style(RenderType("blue"))
    assert str(register.blue) == ""

    # Unmute: previously muted styles must be re-rendered with their original rules.
    register.unmute()
    assert register.is_muted is False
    assert str(register.red) == "\x1b[31m"
    assert register("red") == str(register.red)

    # The attribute that was assigned during muting must now render correctly too.
    assert str(register.blue) == "\x1b[31m"

# Generated at 2026-10-25 01:26:38.171812
# Unit test for method unmute of class Register
def test_Register_unmute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(
        DummyRenderType,
        lambda value: f"<rendered:{value}>",
    )
    register.example = Style(DummyRenderType(42))

    assert register.example == "<rendered:42>"

    register.mute()
    assert register.is_muted is True
    assert register.example == ""

    register.unmute()
    assert register.is_muted is False
    assert register.example == "<rendered:42>"
    assert register.example.rules == (DummyRenderType(42),)

# Generated at 2026-10-25 01:26:50.210074
# Unit test for method unmute of class Register
def test_Register_unmute():register = Register()


# Generated at 2026-10-25 01:26:52.629313
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:26:55.045050
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:26:57.451201
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:26:59.869268
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:27:02.285373
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:27:04.698340
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:27:07.114127
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:27:09.527554
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:27:11.942515
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:27:14.356712
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:27:30.904180
# Unit test for method unmute of class Register
def test_Register_unmute():
    from sty import Register, Style
    from sty.rendertype import Sgr

    r = Register()
    r.set_renderfunc(Sgr, lambda num: f"<sgr-{num}>")
    r.accent = Style(Sgr(1), Sgr(4))

    # Sanity check: unmuted register renders the style.
    assert r.accent == "<sgr-1><sgr-4>"

    # Mute: all styles must render as empty strings.
    r.mute()
    assert r.is_muted is True
    assert r.accent == ""

    # Unmute: styles must be rendered again with the same rules.
    r.unmute()
    assert r.is_muted is False
    assert r.accent == "<sgr-1><sgr-4>"

    # New assignments after unmuting must render normally too.
    r.bold = Style(Sgr(1))
    assert r.bold == "<sgr-1>"

# Generated at 2026-10-25 01:27:45.341648
# Unit test for method unmute of class Register
def test_Register_unmute():register = Register()
register.set_renderfunc(RenderType, lambda value: f"<{value}>")
register.label = Style(RenderType("value"))

register.mute()
assert register.label == ""

register.unmute()
assert register.label == "<value>"

# Generated at 2026-10-25 01:28:06.227934
# Unit test for method unmute of class Register
def test_Register_unmute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(
        DummyRenderType,
        lambda code: f"\x1b[{code}m",
    )
    register.example = Style(DummyRenderType(31))

    assert register.example == "\x1b[31m"

    register.mute()
    assert register.is_muted is True
    assert register.example == ""

    register.unmute()
    assert register.is_muted is False
    assert register.example == "\x1b[31m"

# Generated at 2026-10-25 01:28:08.833489
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:28:11.249893
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:28:13.665939
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:28:16.081536
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:28:38.180531
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 01:28:39.522690
# Unit test for method mute of class Register
def test_Register_mute():
    r = Register()
    r.set_renderfunc(DummyRenderType, lambda x: f"\x1b[{x}m")
    r.red = Style(DummyRenderType("31"))

    # Sanity check: unmuted register renders the ANSI sequence.
    assert str(r.red) == "\x1b[31m"

    r.mute()

    # 1. Mute flag is set.
    assert r.is_muted is True

    # 2. All Style attributes are re-rendered to empty strings,
    #    but their rules are preserved for unmute.
    assert str(r.red) == ""
    assert r.red.rules == (DummyRenderType("31"),)

    # 3. Direct calls return "" while muted.
    assert r("red") == ""

    # 4. New attributes assigned while muted are also blanked.
    r.blue = Style(DummyRenderType("34"))
    assert str(r.blue) == ""

    # 5. Unmute restores everything from the saved rules.
    r.unmute()
    assert r.is_muted is False
    assert str(r.red) == "\x1b[31m"
    assert str(r.blue) == "\x1b[34m"

# Generated at 2026-10-25 01:28:40.853828
# Unit test for method mute of class Register
def test_Register_mute():
    from sty import Register, Style
    from sty.rendertype import RenderType

    class Dummy(RenderType):
        def __init__(self, code: int):
            self.args = (code,)

    r = Register()
    r.renderfuncs[Dummy] = lambda code: f"<{code}>"
    r.eightbit_call = lambda x: f"8bit({x})"
    r.rgb_call = lambda red, green, blue: f"rgb({red},{green},{blue})"

    r.red = Style(Dummy(31))
    assert str(r.red) == "<31>"
    assert r("red") == "<31>"

    r.mute()
    assert r.is_muted is True
    assert str(r.red) == ""
    assert r("red") == ""
    assert r(42) == ""
    assert r(1, 2, 3) == ""
    assert len(r.red.rules) == 1
    assert isinstance(r.red.rules[0], Dummy)
    assert r.red.rules[0].args == (31,)

    r.unmute()
    assert r.is_muted is False
    assert str(r.red) == "<31>"
    assert r("red") == "<31>"
    assert r(42) == "8bit(42)"
    assert r(1, 2, 3) == "rgb(1,2,3)"

# Generated at 2026-10-25 01:28:42.278381
# Unit test for method mute of class Register
def test_Register_mute():
    from sty import Register, Style
    from sty.rendertype import RenderType

    class Dummy(RenderType):
        def __init__(self, code: int):
            self.args = (code,)

    r = Register()
    r.renderfuncs[Dummy] = lambda code: f"<{code}>"
    r.eightbit_call = lambda x: f"8bit({x})"
    r.rgb_call = lambda red, green, blue: f"rgb({red},{green},{blue})"

    r.red = Style(Dummy(31))
    assert str(r.red) == "<31>"
    assert r("red") == "<31>"

    r.mute()
    assert r.is_muted is True
    assert str(r.red) == ""
    assert r("red") == ""
    assert r(42) == ""
    assert r(1, 2, 3) == ""
    assert len(r.red.rules) == 1
    assert isinstance(r.red.rules[0], Dummy)
    assert r.red.rules[0].args == (31,)

    r.unmute()
    assert r.is_muted is False
    assert str(r.red) == "<31>"
    assert r("red") == "<31>"
    assert r(42) == "8bit(42)"
    assert r(1, 2, 3) == "rgb(1,2,3)"

# Generated at 2026-10-25 01:28:52.328498
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class CustomRenderType(RenderType):
        pass

    register = Register()

    def initial_renderer(value: int) -> str:
        return f"<old:{value}>"

    def replacement_renderer(value: int) -> str:
        return f"<new:{value}>"

    # Register an initial renderer and create a style that uses it.
    register.set_renderfunc(CustomRenderType, initial_renderer)
    register.custom = Style(CustomRenderType(42))

    assert register.renderfuncs[CustomRenderType] is initial_renderer
    assert register.custom == "<old:42>"
    assert register.custom.rules == (CustomRenderType(42),)

    # Replacing the renderer should also rerender existing Style attributes.
    register.set_renderfunc(CustomRenderType, replacement_renderer)

    assert register.renderfuncs[CustomRenderType] is replacement_renderer
    assert isinstance(register.custom, Style)
    assert register.custom == "<new:42>"
    assert register.custom.rules == (CustomRenderType(42),)

# Generated at 2026-10-25 01:29:00.965764
# Unit test for method unmute of class Register
def test_Register_unmute():
    class TestRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(TestRenderType, lambda value: f"<{value}>")
    register.test_style = Style(TestRenderType(42))

    assert register.test_style == "<42>"

    register.mute()
    assert register.is_muted is True
    assert register.test_style == ""

    register.unmute()
    assert register.is_muted is False
    assert register.test_style == "<42>"
    assert isinstance(register.test_style, Style)

# Generated at 2026-10-25 01:29:03.557751
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:29:05.973776
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:29:08.398617
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:29:10.812285
# Unit test for method mute of class Register

# Generated at 2026-10-25 01:29:13.227375
# Unit test for method mute of class Register
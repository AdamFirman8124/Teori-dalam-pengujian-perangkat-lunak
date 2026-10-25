

# Generated at 2026-10-25 00:45:11.225373
# Unit test for method as_dict of class Register

# Generated at 2026-10-25 00:45:18.949664
# Unit test for method as_dict of class Register
def test_Register_as_dict():register = Register()

# Generated at 2026-10-25 00:45:35.763249
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 00:45:41.887490
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 00:45:53.971623
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class TestRenderType(RenderType):
        pass

    register = Register()

    initial_renderfunc = lambda value: f"<{value}>"
    register.set_renderfunc(TestRenderType, initial_renderfunc)

    register.example = Style(TestRenderType(42))

    assert register.renderfuncs[TestRenderType] is initial_renderfunc
    assert isinstance(register.example, Style)
    assert register.example == "<42>"

    # Replacing the render function should re-render existing Style attributes.
    replacement_renderfunc = lambda value: f"[{value}]"
    register.set_renderfunc(TestRenderType, replacement_renderfunc)

    assert register.renderfuncs[TestRenderType] is replacement_renderfunc
    assert isinstance(register.example, Style)
    assert register.example == "[42]"
    assert len(tuple(register.example.rules)) == 1
    assert isinstance(tuple(register.example.rules)[0], TestRenderType)

# Generated at 2026-10-25 00:46:07.900833
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():from sty.register import Register, Style

# Generated at 2026-10-25 00:46:16.193212
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    register = Register()

    def render_eightbit(value: int) -> str:
        return f"eightbit:{value}"

    register.renderfuncs[RenderType] = render_eightbit

    register.set_eightbit_call(RenderType)

    assert register.eightbit_call is render_eightbit
    assert register(42) == "eightbit:42"

# Generated at 2026-10-25 00:46:26.125901
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    register = Register()

    def render_eightbit(value: int) -> str:
        return f"eightbit:{value}"

    register.renderfuncs[RenderType] = render_eightbit

    register.set_eightbit_call(RenderType)

    assert register.eightbit_call is render_eightbit
    assert register(42) == "eightbit:42"

# Generated at 2026-10-25 00:46:41.808320
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

# Generated at 2026-10-25 00:46:56.744669
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

# Generated at 2026-10-25 00:46:59.161135
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:47:01.703306
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 00:47:04.118660
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 00:47:06.533095
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 00:47:08.948228
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 00:47:11.363906
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 00:47:13.789356
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 00:47:16.222898
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:47:18.644806
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:47:21.064447
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:47:23.496128
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 00:47:25.915511
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 00:47:28.343367
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 00:47:30.762270
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 00:47:33.176865
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 00:47:40.678712
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 00:47:53.154878
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

# Generated at 2026-10-25 00:47:54.479156
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

# Generated at 2026-10-25 00:48:12.007985
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    import sys
    from unittest.mock import patch

    register = Register()

    original_rules = (object(), object())
    flattened_rules = (object(),)
    source_style = Style(*original_rules, value="previous value")
    rendered_value = "\x1b[31m"

    module = sys.modules[Register.__module__]

    with patch.object(
        module,
        "_render_rules",
        return_value=(rendered_value, flattened_rules),
    ) as render_rules:
        # An unmuted register renders and flattens an assigned Style.
        register.example = source_style

        render_rules.assert_called_once_with(register.renderfuncs, source_style.rules)
        assert isinstance(register.example, Style)
        assert str(register.example) == rendered_value
        assert register.example.rules == flattened_rules

        # A muted register preserves the original rules but stores an empty value.
        render_rules.reset_mock()
        register.is_muted = True
        register.example = source_style

        render_rules.assert_not_called()
        assert isinstance(register.example, Style)
        assert str(register.example) == ""
        assert register.example.rules == source_style.rules

    # Non-Style values are delegated unchanged to object.__setattr__.
    marker = object()
    register.other = marker

    assert register.other is marker

# Generated at 2026-10-25 00:48:14.425707
# Unit test for constructor of class Register

# Generated at 2026-10-25 00:48:16.840995
# Unit test for constructor of class Register

# Generated at 2026-10-25 00:48:19.260568
# Unit test for constructor of class Register

# Generated at 2026-10-25 00:48:21.676692
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:48:24.097810
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:48:26.513646
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:48:28.928295
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 00:48:31.345355
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 00:48:33.772146
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 00:48:36.187294
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:48:38.604539
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:48:41.025646
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:48:43.442442
# Unit test for constructor of class Register

# Generated at 2026-10-25 00:48:47.827185
# Unit test for constructor of class Register
def test_Register():register = Register()

# Generated at 2026-10-25 00:48:49.183334
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

# Generated at 2026-10-25 00:48:58.294004
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class TestRenderType(RenderType):
        pass

    register = Register()
    rule = TestRenderType(42)

    # Register the initial renderer and create a style using it.
    register.set_renderfunc(TestRenderType, lambda value: f"old:{value}")
    register.example = Style(rule)

    assert str(register.example) == "old:42"

    # Replacing the renderer should re-render existing Style attributes.
    new_renderfunc = lambda value: f"new:{value}"
    register.set_renderfunc(TestRenderType, new_renderfunc)

    assert register.renderfuncs[TestRenderType] is new_renderfunc
    assert isinstance(register.example, Style)
    assert str(register.example) == "new:42"
    assert tuple(register.example.rules) == (rule,)

# Generated at 2026-10-25 00:48:59.830218
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():from sty.register import Register, Style

# Generated at 2026-10-25 00:49:01.206124
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

# Generated at 2026-10-25 00:49:14.681064
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class TestRenderType(RenderType):
        pass

    register = Register()

    def first_renderer(*args):
        return f"first:{','.join(map(str, args))}"

    register.set_renderfunc(TestRenderType, first_renderer)

    # The render function is registered.
    assert register.renderfuncs[TestRenderType] is first_renderer

    # New styles use the registered render function.
    rule = TestRenderType(1, 2, 3)
    register.example = Style(rule)
    assert register.example == "first:1,2,3"
    assert tuple(register.example.rules) == (rule,)

    def second_renderer(*args):
        return f"second:{'-'.join(map(str, args))}"

    register.set_renderfunc(TestRenderType, second_renderer)

    # Replacing the function also re-renders existing Style attributes.
    assert register.renderfuncs[TestRenderType] is second_renderer
    assert register.example == "second:1-2-3"
    assert tuple(register.example.rules) == (rule,)

# Generated at 2026-10-25 00:49:24.200182
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class DummyRenderType(RenderType):
        pass

    register = Register()

    def initial_renderer(value):
        return f"<{value}>"

    register.set_renderfunc(DummyRenderType, initial_renderer)
    register.example = Style(DummyRenderType(42))

    assert register.renderfuncs[DummyRenderType] is initial_renderer
    assert register.example == "<42>"
    assert isinstance(register.example, Style)

    def replacement_renderer(value):
        return f"[{value}]"

    register.set_renderfunc(DummyRenderType, replacement_renderer)

    # Existing styles should be re-rendered with the replacement function.
    assert register.renderfuncs[DummyRenderType] is replacement_renderer
    assert register.example == "[42]"
    assert isinstance(register.example, Style)
    assert len(register.example.rules) == 1
    assert isinstance(register.example.rules[0], DummyRenderType)

# Generated at 2026-10-25 00:49:26.617678
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:49:29.032629
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:49:31.450243
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:49:33.869506
# Unit test for method unmute of class Register

# Generated at 2026-10-25 00:49:36.283336
# Unit test for method unmute of class Register

# Generated at 2026-10-25 00:49:38.697258
# Unit test for method unmute of class Register

# Generated at 2026-10-25 00:49:41.307576
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:49:43.721834
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:49:46.138073
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:49:48.552184
# Unit test for method unmute of class Register

# Generated at 2026-10-25 00:49:50.967676
# Unit test for method unmute of class Register

# Generated at 2026-10-25 00:49:53.382380
# Unit test for method unmute of class Register

# Generated at 2026-10-25 00:49:55.797500
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:49:58.213462
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:50:00.640805
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:50:03.054851
# Unit test for method unmute of class Register

# Generated at 2026-10-25 00:50:05.472477
# Unit test for method unmute of class Register

# Generated at 2026-10-25 00:50:07.888545
# Unit test for method unmute of class Register

# Generated at 2026-10-25 00:50:10.305939
# Unit test for method unmute of class Register

# Generated at 2026-10-25 00:50:35.062687
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

# Generated at 2026-10-25 00:50:36.394080
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

# Generated at 2026-10-25 00:50:37.722412
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

# Generated at 2026-10-25 00:50:39.051684
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

# Generated at 2026-10-25 00:50:40.391511
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

# Generated at 2026-10-25 00:50:41.819202
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

# Generated at 2026-10-25 00:50:43.137080
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

# Generated at 2026-10-25 00:50:45.815117
# Unit test for method unmute of class Register

# Generated at 2026-10-25 00:50:48.230382
# Unit test for method unmute of class Register

# Generated at 2026-10-25 00:50:50.645655
# Unit test for method unmute of class Register

# Generated at 2026-10-25 00:50:53.192694
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:50:55.619282
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:50:58.064710
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:51:00.503576
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:51:02.945201
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:51:05.367854
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:51:07.784370
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:51:10.199768
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:51:12.614072
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:51:15.029840
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:51:17.445228
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:51:19.875344
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:51:22.319335
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:51:46.528509
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:51:47.901078
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

# Generated at 2026-10-25 00:52:01.795110
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class TestRenderType(RenderType):
        pass

    register = Register()

    def initial_renderer(value: int) -> str:
        return f"<old:{value}>"

    register.set_renderfunc(TestRenderType, initial_renderer)

    assert register.renderfuncs[TestRenderType] is initial_renderer

    register.example = Style(TestRenderType(42))
    assert register.example == "<old:42>"

    def replacement_renderer(value: int) -> str:
        return f"<new:{value}>"

    register.set_renderfunc(TestRenderType, replacement_renderer)

    # The renderer is replaced and existing Style attributes are re-rendered.
    assert register.renderfuncs[TestRenderType] is replacement_renderer
    assert register.example == "<new:42>"
    assert len(tuple(register.example.rules)) == 1
    assert isinstance(tuple(register.example.rules)[0], TestRenderType)

# Generated at 2026-10-25 00:52:15.400237
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    class TestRenderType(RenderType):
        pass

    register = Register()

    def initial_renderer(value):
        return f"<initial:{value}>"

    def replacement_renderer(value):
        return f"<replacement:{value}>"

    # Register the initial renderer.
    register.set_renderfunc(TestRenderType, initial_renderer)

    assert register.renderfuncs[TestRenderType] is initial_renderer

    # Styles assigned to the register use the registered renderer.
    register.example = Style(TestRenderType(42))

    assert isinstance(register.example, Style)
    assert str(register.example) == "<initial:42>"

    # Replacing the renderer re-renders existing Style attributes.
    register.set_renderfunc(TestRenderType, replacement_renderer)

    assert register.renderfuncs[TestRenderType] is replacement_renderer
    assert str(register.example) == "<replacement:42>"
    assert register.example.rules == (TestRenderType(42),)

# Generated at 2026-10-25 00:52:17.818044
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:52:20.233001
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:52:22.657600
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:52:25.072840
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:52:27.491742
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:52:29.907260
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:52:32.321271
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:52:34.735800
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:52:37.150626
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:52:38.489949
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

# Generated at 2026-10-25 00:52:39.813737
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

# Generated at 2026-10-25 00:52:41.209341
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

# Generated at 2026-10-25 00:52:45.348246
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

# Generated at 2026-10-25 00:52:46.671066
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

# Generated at 2026-10-25 00:52:48.078871
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

# Generated at 2026-10-25 00:52:49.512312
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

# Generated at 2026-10-25 00:52:50.834608
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

# Generated at 2026-10-25 00:52:52.169729
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

# Generated at 2026-10-25 00:52:53.502411
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

# Generated at 2026-10-25 00:52:54.832658
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

# Generated at 2026-10-25 00:52:56.170902
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

# Generated at 2026-10-25 00:52:57.505606
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

# Generated at 2026-10-25 00:52:58.850433
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

# Generated at 2026-10-25 00:53:00.196671
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

# Generated at 2026-10-25 00:53:01.528549
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

# Generated at 2026-10-25 00:53:02.847264
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

# Generated at 2026-10-25 00:53:04.186414
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

# Generated at 2026-10-25 00:53:05.590000
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

# Generated at 2026-10-25 00:53:06.938529
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

# Generated at 2026-10-25 00:53:08.331487
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

# Generated at 2026-10-25 00:53:09.660074
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

# Generated at 2026-10-25 00:53:12.077168
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:14.494075
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:17.029316
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:19.446735
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:21.863657
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:24.279402
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:26.695045
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:29.110909
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:31.524899
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:33.941465
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:36.357782
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:42.735346
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:45.153066
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:47.570105
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:49.985913
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:52.409742
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:54.814555
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:57.229452
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:53:59.642764
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:54:02.059267
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:54:03.412232
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

# Generated at 2026-10-25 00:54:04.779323
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

# Generated at 2026-10-25 00:54:06.210301
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

# Generated at 2026-10-25 00:54:07.644716
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

# Generated at 2026-10-25 00:54:08.971880
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

# Generated at 2026-10-25 00:54:10.294440
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

# Generated at 2026-10-25 00:54:11.613308
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

# Generated at 2026-10-25 00:54:12.935997
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

# Generated at 2026-10-25 00:54:14.270812
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

# Generated at 2026-10-25 00:54:15.612284
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

# Generated at 2026-10-25 00:54:16.965430
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

# Generated at 2026-10-25 00:54:18.289422
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

# Generated at 2026-10-25 00:54:19.609863
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

# Generated at 2026-10-25 00:54:20.940227
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

# Generated at 2026-10-25 00:54:22.264258
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

# Generated at 2026-10-25 00:54:23.619556
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

# Generated at 2026-10-25 00:54:26.041744
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:54:28.455340
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:54:30.871616
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:54:33.286382
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:54:35.701089
# Unit test for method mute of class Register

# Generated at 2026-10-25 00:54:50.758337
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 00:54:53.174188
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 00:54:55.589182
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 00:54:58.002834
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:55:00.418967
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:55:02.835944
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 00:55:05.250078
# Unit test for method as_dict of class Register

# Generated at 2026-10-25 00:55:07.664750
# Unit test for method as_dict of class Register

# Generated at 2026-10-25 00:55:10.079136
# Unit test for method as_dict of class Register
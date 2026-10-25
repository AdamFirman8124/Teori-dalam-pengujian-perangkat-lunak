

# Generated at 2026-10-24 11:17:30.558319
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    from .rendertype import RenderType

    class DummyA(RenderType):
        pass

    class DummyB(RenderType):
        pass

    def render_a(x):
        return f"A({x})"

    def render_b(x):
        return f"B({x})"

    # 1. Set up register with two render functions.
    r = Register()
    r.renderfuncs = {DummyA: render_a, DummyB: render_b}

    # 2. Default eightbit_call is the identity lambda.
    assert r.eightbit_call(42) == 42

    # 3. module_0.set_eightbit_call(DummyA) must bind render_a.
    r.set_eightbit_call(DummyA)
    assert r.eightbit_call is render_a
    assert r.eightbit_call(42) == "A(42)"

    # 4. Switching to DummyB must swap it to render_b.
    r.set_eightbit_call(DummyB)
    assert r.eightbit_call is render_b
    assert r.eightbit_call(42) == "B(42)"

    # 5. rgb_call must be untouched by set_eightbit_call.
    assert r.rgb_call(1, 2, 3) == (1, 2, 3)

# Generated at 2026-10-24 11:17:32.985376
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 11:17:35.407226
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 11:17:37.828104
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 11:17:40.249323
# Unit test for method copy of class Register

# Generated at 2026-10-24 11:17:42.805271
# Unit test for method copy of class Register

# Generated at 2026-10-24 11:17:45.221560
# Unit test for method copy of class Register

# Generated at 2026-10-24 11:17:47.643596
# Unit test for method unmute of class Register

# Generated at 2026-10-24 11:18:07.002161
# Unit test for method unmute of class Register

# Generated at 2026-10-24 11:18:27.877968
# Unit test for method unmute of class Register

# Generated at 2026-10-24 11:18:30.395509
# Unit test for method copy of class Register

# Generated at 2026-10-24 11:18:32.910070
# Unit test for method copy of class Register

# Generated at 2026-10-24 11:18:35.336351
# Unit test for method copy of class Register

# Generated at 2026-10-24 11:18:37.753300
# Unit test for method unmute of class Register

# Generated at 2026-10-24 11:18:40.174737
# Unit test for method unmute of class Register

# Generated at 2026-10-24 11:18:42.596290
# Unit test for method unmute of class Register

# Generated at 2026-10-24 11:18:45.020563
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:18:47.439858
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:18:49.857437
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:19:07.320575
# Unit test for method unmute of class Register
def test_Register_unmute():
    from sty import fg
    from sty.rendertype import Sgr

    register = fg.copy()          # don't mutate the global register
    register.my_style = Style(Sgr(1))

    expected = register.renderfuncs[Sgr](1)   # '\x1b[1m'

    # rendered on set
    assert register.my_style == expected
    assert isinstance(register.my_style, Style)

    # muted -> empty string, rules kept
    register.mute()
    assert register.is_muted is True
    assert register.my_style == ""
    assert register.my_style.rules

    # unmuted -> rendered again
    register.unmute()
    assert register.is_muted is False
    assert register.my_style == expected
    assert isinstance(register.my_style, Style)

# Generated at 2026-10-24 11:19:31.177572
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    from .rendertype import RenderType

    # --- Minimal fake rendertypes + renderfuncs ---------------------------
    class DummyFg(RenderType):
        pass

    class DummyBold(RenderType):
        pass

    renderfuncs = {
        DummyFg: lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m",
        DummyBold: lambda: "\x1b[1m",
    }

    # --- 1. Unmuted: Style value is rendered and rules are flattened ------
    reg = Register()
    reg.renderfuncs = renderfuncs
    reg.is_muted = False

    reg.orange = Style(DummyFg(1, 5, 10), DummyBold())

    assert isinstance(reg.orange, Style)
    assert str(reg.orange) == "\x1b[38;2;1;5;10m\x1b[1m"
    # rules are replaced by the flattened, already-rendered rule list
    assert all(isinstance(r, RenderType) for r in reg.orange.rules)
    assert len(reg.orange.rules) == 2

    # --- 2. Nested Styles are flattened recursively -----------------------
    reg.mixed = Style(DummyBold(), Style(DummyFg(0, 0, 0)))

    assert str(reg.mixed) == "\x1b[1m\x1b[38;2;0;0;0m"
    assert len(reg.mixed.rules) == 2  # inner Style expanded, no nesting left

    # --- 3. Muted: value becomes "", but rules are kept for later unmute --
    reg.mute()
    reg.blue = Style(DummyFg(0, 0, 255), DummyBold())

    assert str(reg.blue) == ""
    assert len(reg.blue.rules) == 2  # rules preserved, not rendered

    # --- 4. Unmute re-renders previously muted styles ---------------------
    reg.unmute()
    # unmute() re-runs __setattr__ on all existing Style attributes
    assert str(reg.blue) == "\x1b[38;2;0;0;255m\x1b[1m"

    # --- 5. Non-Style values pass through untouched ------------------------
    reg.is_muted = True  # even when muted
    reg.not_a_style = 42
    reg.also_not = "plain string"

    assert reg.not_a_style == 42
    assert reg.also_not == "plain string"

# Generated at 2026-10-24 11:19:33.600564
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:19:36.022820
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:19:38.441611
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:19:40.862659
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:19:43.285140
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:19:45.704494
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 11:19:48.123599
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 11:19:50.539241
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 11:19:52.955988
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:19:55.371767
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:19:57.787992
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:20:00.206493
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 11:20:02.623628
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 11:20:05.043703
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 11:20:07.462350
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:20:09.878945
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:20:12.298362
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:20:14.717901
# Unit test for method unmute of class Register

# Generated at 2026-10-24 11:20:17.133160
# Unit test for method unmute of class Register

# Generated at 2026-10-24 11:20:19.552332
# Unit test for method unmute of class Register

# Generated at 2026-10-24 11:21:35.183658
# Unit test for method mute of class Register
def test_Register_mute():
    from .rendertype import Sgr, EightbitFg, RgbFg

    # Create a register and register render-functions for the render types.
    r = Register()
    r.set_renderfunc(Sgr, lambda code: f"\x1b[{code}m")
    r.set_renderfunc(EightbitFg, lambda code: f"\x1b[38;5;{code}m")
    r.set_renderfunc(RgbFg, lambda r_, g_, b_: f"\x1b[38;2;{r_};{g_};{b_}m")
    r.set_eightbit_call(EightbitFg)
    r.set_rgb_call(RgbFg)

    # Create some styles on the register.
    r.orange = Style(RgbFg(255, 100, 0), Sgr(1))
    r.blue = Style(RgbFg(0, 0, 255))

    # Sanity-check the rendered styles before muting.
    assert str(r.orange) == "\x1b[38;2;255;100;0m\x1b[1m"
    assert str(r.blue) == "\x1b[38;2;0;0;255m"
    assert r(42) == "\x1b[38;5;42m"
    assert r(10, 20, 30) == "\x1b[38;2;10;20;30m"

    # Mute the register.
    r.mute()
    assert r.is_muted is True

    # Existing styles are re-rendered to empty strings.
    assert str(r.orange) == ""
    assert str(r.blue) == ""

    # Styles assigned while muted are also rendered to empty strings.
    r.green = Style(RgbFg(0, 255, 0), Sgr(1))
    assert str(r.green) == ""

    # Direct calls return empty strings while muted.
    assert r(42) == ""
    assert r(1, 2, 3) == ""
    assert r("orange") == ""

    # Unmute the register.
    r.unmute()
    assert r.is_muted is False

    # All styles (including the one created while muted) are re-rendered
    # with their original rules intact.
    assert str(r.orange) == "\x1b[38;2;255;100;0m\x1b[1m"
    assert str(r.blue) == "\x1b[38;2;0;0;255m"
    assert str(r.green) == "\x1b[38;2;0;255;0m\x1b[1m"

    # Direct calls work again after unmuting.
    assert r(42) == "\x1b[38;5;42m"
    assert r(10, 20, 30) == "\x1b[38;2;10;20;30m"
    assert r("orange") == "\x1b[38;2;255;100;0m\x1b[1m"

# Generated at 2026-10-24 11:22:07.600935
# Unit test for method mute of class Register
def test_Register_mute():from sty.register import Register, Style

# Generated at 2026-10-24 11:22:10.135237
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 11:22:12.557212
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 11:22:15.021260
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 11:22:17.440544
# Unit test for constructor of class Register

# Generated at 2026-10-24 11:22:19.861623
# Unit test for constructor of class Register

# Generated at 2026-10-24 11:22:22.276665
# Unit test for constructor of class Register

# Generated at 2026-10-24 11:22:24.696968
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 11:22:27.115714
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 11:22:44.306579
# Unit test for method __call__ of class Register
def test_Register___call__():from sty import Register, Style


# Generated at 2026-10-24 11:22:45.671509
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    from .rendertype import RenderType

    # --- Minimal fake rendertypes + renderfuncs ---------------------------
    class DummyFg(RenderType):
        pass

    class DummyBold(RenderType):
        pass

    renderfuncs = {
        DummyFg: lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m",
        DummyBold: lambda: "\x1b[1m",
    }

    # --- 1. Unmuted: Style value is rendered and rules are flattened ------
    reg = Register()
    reg.renderfuncs = renderfuncs
    reg.is_muted = False

    reg.orange = Style(DummyFg(1, 5, 10), DummyBold())

    assert isinstance(reg.orange, Style)
    assert str(reg.orange) == "\x1b[38;2;1;5;10m\x1b[1m"
    # rules are replaced by the flattened, already-rendered rule list
    assert all(isinstance(r, RenderType) for r in reg.orange.rules)
    assert len(reg.orange.rules) == 2

    # --- 2. Nested Styles are flattened recursively -----------------------
    reg.mixed = Style(DummyBold(), Style(DummyFg(0, 0, 0)))

    assert str(reg.mixed) == "\x1b[1m\x1b[38;2;0;0;0m"
    assert len(reg.mixed.rules) == 2  # inner Style expanded, no nesting left

    # --- 3. Muted: value becomes "", but rules are kept for later unmute --
    reg.mute()
    reg.blue = Style(DummyFg(0, 0, 255), DummyBold())

    assert str(reg.blue) == ""
    assert len(reg.blue.rules) == 2  # rules preserved, not rendered

    # --- 4. Unmute re-renders previously muted styles ---------------------
    reg.unmute()
    # unmute() re-runs __setattr__ on all existing Style attributes
    assert str(reg.blue) == "\x1b[38;2;0;0;255m\x1b[1m"

    # --- 5. Non-Style values pass through untouched ------------------------
    reg.is_muted = True  # even when muted
    reg.not_a_style = 42
    reg.also_not = "plain string"

    assert reg.not_a_style == 42
    assert reg.also_not == "plain string"

# Generated at 2026-10-24 11:23:13.932089
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():reg = Register()

    # Setting a Style attribute re-renders it through the register.
    # With no render rules, the rendered value is the empty string,
    # but the rules must be preserved on the stored Style.

# Generated at 2026-10-24 11:23:15.330568
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    from .rendertype import RenderType

    # --- Minimal fake rendertypes + renderfuncs ---------------------------
    class DummyFg(RenderType):
        pass

    class DummyBold(RenderType):
        pass

    renderfuncs = {
        DummyFg: lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m",
        DummyBold: lambda: "\x1b[1m",
    }

    # --- 1. Unmuted: Style value is rendered and rules are flattened ------
    reg = Register()
    reg.renderfuncs = renderfuncs
    reg.is_muted = False

    reg.orange = Style(DummyFg(1, 5, 10), DummyBold())

    assert isinstance(reg.orange, Style)
    assert str(reg.orange) == "\x1b[38;2;1;5;10m\x1b[1m"
    # rules are replaced by the flattened, already-rendered rule list
    assert all(isinstance(r, RenderType) for r in reg.orange.rules)
    assert len(reg.orange.rules) == 2

    # --- 2. Nested Styles are flattened recursively -----------------------
    reg.mixed = Style(DummyBold(), Style(DummyFg(0, 0, 0)))

    assert str(reg.mixed) == "\x1b[1m\x1b[38;2;0;0;0m"
    assert len(reg.mixed.rules) == 2  # inner Style expanded, no nesting left

    # --- 3. Muted: value becomes "", but rules are kept for later unmute --
    reg.mute()
    reg.blue = Style(DummyFg(0, 0, 255), DummyBold())

    assert str(reg.blue) == ""
    assert len(reg.blue.rules) == 2  # rules preserved, not rendered

    # --- 4. Unmute re-renders previously muted styles ---------------------
    reg.unmute()
    # unmute() re-runs __setattr__ on all existing Style attributes
    assert str(reg.blue) == "\x1b[38;2;0;0;255m\x1b[1m"

    # --- 5. Non-Style values pass through untouched ------------------------
    reg.is_muted = True  # even when muted
    reg.not_a_style = 42
    reg.also_not = "plain string"

    assert reg.not_a_style == 42
    assert reg.also_not == "plain string"

# Generated at 2026-10-24 11:23:18.531974
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():reg = Register()

    # Setting a Style attribute re-renders it through the register.
    # With no render rules, the rendered value is the empty string,
    # but the rules must be preserved on the stored Style.

# Generated at 2026-10-24 11:23:19.849897
# Unit test for method unmute of class Register
def test_Register_unmute():
    from sty import fg
    from sty.rendertype import Sgr

    register = fg.copy()          # don't mutate the global register
    register.my_style = Style(Sgr(1))

    expected = register.renderfuncs[Sgr](1)   # '\x1b[1m'

    # rendered on set
    assert register.my_style == expected
    assert isinstance(register.my_style, Style)

    # muted -> empty string, rules kept
    register.mute()
    assert register.is_muted is True
    assert register.my_style == ""
    assert register.my_style.rules

    # unmuted -> rendered again
    register.unmute()
    assert register.is_muted is False
    assert register.my_style == expected
    assert isinstance(register.my_style, Style)

# Generated at 2026-10-24 11:23:21.172620
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    from .rendertype import RenderType

    # --- Minimal fake rendertypes + renderfuncs ---------------------------
    class DummyFg(RenderType):
        pass

    class DummyBold(RenderType):
        pass

    renderfuncs = {
        DummyFg: lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m",
        DummyBold: lambda: "\x1b[1m",
    }

    # --- 1. Unmuted: Style value is rendered and rules are flattened ------
    reg = Register()
    reg.renderfuncs = renderfuncs
    reg.is_muted = False

    reg.orange = Style(DummyFg(1, 5, 10), DummyBold())

    assert isinstance(reg.orange, Style)
    assert str(reg.orange) == "\x1b[38;2;1;5;10m\x1b[1m"
    # rules are replaced by the flattened, already-rendered rule list
    assert all(isinstance(r, RenderType) for r in reg.orange.rules)
    assert len(reg.orange.rules) == 2

    # --- 2. Nested Styles are flattened recursively -----------------------
    reg.mixed = Style(DummyBold(), Style(DummyFg(0, 0, 0)))

    assert str(reg.mixed) == "\x1b[1m\x1b[38;2;0;0;0m"
    assert len(reg.mixed.rules) == 2  # inner Style expanded, no nesting left

    # --- 3. Muted: value becomes "", but rules are kept for later unmute --
    reg.mute()
    reg.blue = Style(DummyFg(0, 0, 255), DummyBold())

    assert str(reg.blue) == ""
    assert len(reg.blue.rules) == 2  # rules preserved, not rendered

    # --- 4. Unmute re-renders previously muted styles ---------------------
    reg.unmute()
    # unmute() re-runs __setattr__ on all existing Style attributes
    assert str(reg.blue) == "\x1b[38;2;0;0;255m\x1b[1m"

    # --- 5. Non-Style values pass through untouched ------------------------
    reg.is_muted = True  # even when muted
    reg.not_a_style = 42
    reg.also_not = "plain string"

    assert reg.not_a_style == 42
    assert reg.also_not == "plain string"

# Generated at 2026-10-24 11:23:23.708697
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:23:26.126124
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:23:28.714361
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:23:31.132825
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:23:33.552757
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:23:34.951639
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    from .rendertype import RenderType

    # --- Minimal fake rendertypes + renderfuncs ---------------------------
    class DummyFg(RenderType):
        pass

    class DummyBold(RenderType):
        pass

    renderfuncs = {
        DummyFg: lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m",
        DummyBold: lambda: "\x1b[1m",
    }

    # --- 1. Unmuted: Style value is rendered and rules are flattened ------
    reg = Register()
    reg.renderfuncs = renderfuncs
    reg.is_muted = False

    reg.orange = Style(DummyFg(1, 5, 10), DummyBold())

    assert isinstance(reg.orange, Style)
    assert str(reg.orange) == "\x1b[38;2;1;5;10m\x1b[1m"
    # rules are replaced by the flattened, already-rendered rule list
    assert all(isinstance(r, RenderType) for r in reg.orange.rules)
    assert len(reg.orange.rules) == 2

    # --- 2. Nested Styles are flattened recursively -----------------------
    reg.mixed = Style(DummyBold(), Style(DummyFg(0, 0, 0)))

    assert str(reg.mixed) == "\x1b[1m\x1b[38;2;0;0;0m"
    assert len(reg.mixed.rules) == 2  # inner Style expanded, no nesting left

    # --- 3. Muted: value becomes "", but rules are kept for later unmute --
    reg.mute()
    reg.blue = Style(DummyFg(0, 0, 255), DummyBold())

    assert str(reg.blue) == ""
    assert len(reg.blue.rules) == 2  # rules preserved, not rendered

    # --- 4. Unmute re-renders previously muted styles ---------------------
    reg.unmute()
    # unmute() re-runs __setattr__ on all existing Style attributes
    assert str(reg.blue) == "\x1b[38;2;0;0;255m\x1b[1m"

    # --- 5. Non-Style values pass through untouched ------------------------
    reg.is_muted = True  # even when muted
    reg.not_a_style = 42
    reg.also_not = "plain string"

    assert reg.not_a_style == 42
    assert reg.also_not == "plain string"

# Generated at 2026-10-24 11:23:37.857228
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():reg = Register()

    # Setting a Style attribute re-renders it through the register.
    # With no render rules, the rendered value is the empty string,
    # but the rules must be preserved on the stored Style.

# Generated at 2026-10-24 11:23:39.168176
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    from .rendertype import RenderType

    # --- Minimal fake rendertypes + renderfuncs ---------------------------
    class DummyFg(RenderType):
        pass

    class DummyBold(RenderType):
        pass

    renderfuncs = {
        DummyFg: lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m",
        DummyBold: lambda: "\x1b[1m",
    }

    # --- 1. Unmuted: Style value is rendered and rules are flattened ------
    reg = Register()
    reg.renderfuncs = renderfuncs
    reg.is_muted = False

    reg.orange = Style(DummyFg(1, 5, 10), DummyBold())

    assert isinstance(reg.orange, Style)
    assert str(reg.orange) == "\x1b[38;2;1;5;10m\x1b[1m"
    # rules are replaced by the flattened, already-rendered rule list
    assert all(isinstance(r, RenderType) for r in reg.orange.rules)
    assert len(reg.orange.rules) == 2

    # --- 2. Nested Styles are flattened recursively -----------------------
    reg.mixed = Style(DummyBold(), Style(DummyFg(0, 0, 0)))

    assert str(reg.mixed) == "\x1b[1m\x1b[38;2;0;0;0m"
    assert len(reg.mixed.rules) == 2  # inner Style expanded, no nesting left

    # --- 3. Muted: value becomes "", but rules are kept for later unmute --
    reg.mute()
    reg.blue = Style(DummyFg(0, 0, 255), DummyBold())

    assert str(reg.blue) == ""
    assert len(reg.blue.rules) == 2  # rules preserved, not rendered

    # --- 4. Unmute re-renders previously muted styles ---------------------
    reg.unmute()
    # unmute() re-runs __setattr__ on all existing Style attributes
    assert str(reg.blue) == "\x1b[38;2;0;0;255m\x1b[1m"

    # --- 5. Non-Style values pass through untouched ------------------------
    reg.is_muted = True  # even when muted
    reg.not_a_style = 42
    reg.also_not = "plain string"

    assert reg.not_a_style == 42
    assert reg.also_not == "plain string"

# Generated at 2026-10-24 11:23:57.004360
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():reg = Register()

    # Setting a Style attribute re-renders it through the register.
    # With no render rules, the rendered value is the empty string,
    # but the rules must be preserved on the stored Style.

# Generated at 2026-10-24 11:23:58.317460
# Unit test for method unmute of class Register
def test_Register_unmute():
    from sty import fg
    from sty.rendertype import Sgr

    register = fg.copy()          # don't mutate the global register
    register.my_style = Style(Sgr(1))

    expected = register.renderfuncs[Sgr](1)   # '\x1b[1m'

    # rendered on set
    assert register.my_style == expected
    assert isinstance(register.my_style, Style)

    # muted -> empty string, rules kept
    register.mute()
    assert register.is_muted is True
    assert register.my_style == ""
    assert register.my_style.rules

    # unmuted -> rendered again
    register.unmute()
    assert register.is_muted is False
    assert register.my_style == expected
    assert isinstance(register.my_style, Style)

# Generated at 2026-10-24 11:25:07.461624
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 11:25:19.951830
# Unit test for method as_dict of class Register
def test_Register_as_dict():from sty.rendertype import Sgr

reg = Register()
reg.red = "31-red-value"
reg.blue = "94-blue-value"
reg._hidden = "should-not-appear"
reg.is_muted = False  # non-str attributes must be excluded

assert reg.as_dict() == {"red": "31-red-value", "blue": "94-blue-value"}

reg2 = Register()
reg2.renderfuncs = {Sgr: lambda x: f"\x1b[{x}m"}
reg2.bold = Style(Sgr(1))
reg2.dim = Style(Sgr(2))

assert reg2.as_dict() == {"bold": "\x1b[1m", "dim": "\x1b[2m"}

# Generated at 2026-10-24 11:25:22.646167
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:25:25.068276
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:25:27.489269
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 11:25:29.910176
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 11:25:32.501144
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 11:25:34.918828
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 11:25:37.337443
# Unit test for method mute of class Register

# Generated at 2026-10-24 11:25:39.761119
# Unit test for method mute of class Register

# Generated at 2026-10-24 11:25:42.177133
# Unit test for method mute of class Register

# Generated at 2026-10-24 11:25:59.965493
# Unit test for method mute of class Register
def test_Register_mute():
    from .rendertype import Sgr, EightbitFg, RgbFg

    # Create a register and register render-functions for the render types.
    r = Register()
    r.set_renderfunc(Sgr, lambda code: f"\x1b[{code}m")
    r.set_renderfunc(EightbitFg, lambda code: f"\x1b[38;5;{code}m")
    r.set_renderfunc(RgbFg, lambda r_, g_, b_: f"\x1b[38;2;{r_};{g_};{b_}m")
    r.set_eightbit_call(EightbitFg)
    r.set_rgb_call(RgbFg)

    # Create some styles on the register.
    r.orange = Style(RgbFg(255, 100, 0), Sgr(1))
    r.blue = Style(RgbFg(0, 0, 255))

    # Sanity-check the rendered styles before muting.
    assert str(r.orange) == "\x1b[38;2;255;100;0m\x1b[1m"
    assert str(r.blue) == "\x1b[38;2;0;0;255m"
    assert r(42) == "\x1b[38;5;42m"
    assert r(10, 20, 30) == "\x1b[38;2;10;20;30m"

    # Mute the register.
    r.mute()
    assert r.is_muted is True

    # Existing styles are re-rendered to empty strings.
    assert str(r.orange) == ""
    assert str(r.blue) == ""

    # Styles assigned while muted are also rendered to empty strings.
    r.green = Style(RgbFg(0, 255, 0), Sgr(1))
    assert str(r.green) == ""

    # Direct calls return empty strings while muted.
    assert r(42) == ""
    assert r(1, 2, 3) == ""
    assert r("orange") == ""

    # Unmute the register.
    r.unmute()
    assert r.is_muted is False

    # All styles (including the one created while muted) are re-rendered
    # with their original rules intact.
    assert str(r.orange) == "\x1b[38;2;255;100;0m\x1b[1m"
    assert str(r.blue) == "\x1b[38;2;0;0;255m"
    assert str(r.green) == "\x1b[38;2;0;255;0m\x1b[1m"

    # Direct calls work again after unmuting.
    assert r(42) == "\x1b[38;5;42m"
    assert r(10, 20, 30) == "\x1b[38;2;10;20;30m"
    assert r("orange") == "\x1b[38;2;255;100;0m\x1b[1m"

# Generated at 2026-10-24 11:26:02.742464
# Unit test for method mute of class Register
def test_Register_mute():from sty.register import Register, Style

# Generated at 2026-10-24 11:26:04.146908
# Unit test for method unmute of class Register
def test_Register_unmute():
    from sty import fg
    from sty.rendertype import Sgr

    register = fg.copy()          # don't mutate the global register
    register.my_style = Style(Sgr(1))

    expected = register.renderfuncs[Sgr](1)   # '\x1b[1m'

    # rendered on set
    assert register.my_style == expected
    assert isinstance(register.my_style, Style)

    # muted -> empty string, rules kept
    register.mute()
    assert register.is_muted is True
    assert register.my_style == ""
    assert register.my_style.rules

    # unmuted -> rendered again
    register.unmute()
    assert register.is_muted is False
    assert register.my_style == expected
    assert isinstance(register.my_style, Style)

# Generated at 2026-10-24 11:26:06.951175
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 11:26:08.387219
# Unit test for method as_dict of class Register
def test_Register_as_dict():from sty.rendertype import Sgr

reg = Register()
reg.red = "31-red-value"
reg.blue = "94-blue-value"
reg._hidden = "should-not-appear"
reg.is_muted = False  # non-str attributes must be excluded

assert reg.as_dict() == {"red": "31-red-value", "blue": "94-blue-value"}

reg2 = Register()
reg2.renderfuncs = {Sgr: lambda x: f"\x1b[{x}m"}
reg2.bold = Style(Sgr(1))
reg2.dim = Style(Sgr(2))

assert reg2.as_dict() == {"bold": "\x1b[1m", "dim": "\x1b[2m"}

# Generated at 2026-10-24 11:26:41.630965
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 11:26:44.234007
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 11:26:46.657581
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 11:27:12.673486
# Unit test for method __call__ of class Register
def test_Register___call__():
    from sty import Register, Style, RenderType
    from typing import Callable, Dict, Type

    # --- Custom render types for testing -------------------------------------
    class EightBit(RenderType):
        def __init__(self, x: int):
            self.args = (x,)

    class Rgb(RenderType):
        def __init__(self, r: int, g: int, b: int):
            self.args = (r, g, b)

    def eightbit_render(x: int) -> str:
        return f"\x1b[38;5;{x}m"

    def rgb_render(r: int, g: int, b: int) -> str:
        return f"\x1b[38;2;{r};{g};{b}m"

    # --- Setup ----------------------------------------------------------------
    register = Register()
    register.renderfuncs = {
        EightBit: eightbit_render,
        Rgb: rgb_render,
    }
    register.set_eightbit_call(EightBit)
    register.set_rgb_call(Rgb)

    # Populate a named style attribute (e.g. like fg.red)
    setattr(register, "red", Style(EightBit(9)))

    # --- 1. Single int arg -> eightbit_call -----------------------------------
    result = register(42)
    assert result == "\x1b[38;5;42m", f"Expected 8bit render, got {result!r}"

    # --- 2. Single str arg -> returns named attribute -------------------------
    result = register("red")
    assert result == "\x1b[38;5;9m", f"Expected named style, got {result!r}"

    # --- 3. Three int args -> rgb_call ----------------------------------------
    result = register(10, 42, 255)
    assert result == "\x1b[38;2;10;42;255m", f"Expected rgb render, got {result!r}"

    # --- 4. Wrong number of args -> empty string ------------------------------
    result = register()
    assert result == "", f"Expected '', got {result!r}"

    result = register(1, 2)
    assert result == "", f"Expected '', got {result!r}"

    result = register(1, 2, 3, 4)
    assert result == "", f"Expected '', got {result!r}"

    # --- 5. Unknown attribute name raises AttributeError ----------------------
    try:
        register("nonexistent_color")
        raised = False
    except AttributeError:
        raised = True
    assert raised, "Expected AttributeError for unknown attribute name"

    # --- 6. Muted register always returns empty string -------------------------
    register.mute()
    assert register(42) == ""
    assert register(10, 42, 255) == ""
    assert register("red") == ""

    # --- 7. Unmute restores normal behavior ------------------------------------
    register.unmute()
    assert register(42) == "\x1b[38;5;42m"
    assert register(10, 42, 255) == "\x1b[38;2;10;42;255m"
    assert register("red") == "\x1b[38;5;9m"

    # --- 8. Default register (no renderfuncs set) falls back to lambdas --------
    plain = Register()
    assert plain(42) == 42            # default eightbit_call is identity
    assert plain(1, 2, 3) == (1, 2, 3)  # default rgb_call returns tuple

    # --- 9. Non-int, non-str single arg -> falls to getattr path ----------------
    # e.g. a float is not an int, so it goes to getattr and raises AttributeError
    try:
        plain(3.14)
        raised = False
    except AttributeError:
        raised = True
    assert raised, "Expected AttributeError for unsupported single-arg type"

# Generated at 2026-10-24 11:27:15.321418
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 11:27:16.641537
# Unit test for method as_dict of class Register
def test_Register_as_dict():from sty.rendertype import Sgr

reg = Register()
reg.red = "31-red-value"
reg.blue = "94-blue-value"
reg._hidden = "should-not-appear"
reg.is_muted = False  # non-str attributes must be excluded

assert reg.as_dict() == {"red": "31-red-value", "blue": "94-blue-value"}

reg2 = Register()
reg2.renderfuncs = {Sgr: lambda x: f"\x1b[{x}m"}
reg2.bold = Style(Sgr(1))
reg2.dim = Style(Sgr(2))

assert reg2.as_dict() == {"bold": "\x1b[1m", "dim": "\x1b[2m"}

# Generated at 2026-10-24 11:27:19.293306
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 11:27:21.812804
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 11:27:24.229526
# Unit test for method as_dict of class Register
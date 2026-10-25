

# Generated at 2026-10-24 20:30:05.686815
# Unit test for method copy of class Register
def test_Register_copy():
    register = Register()
    register.custom_data = {"colors": ["red", "green"]}
    register.is_muted = True

    copied_register = register.copy()

    assert copied_register is not register
    assert copied_register.__dict__ == register.__dict__
    assert copied_register.renderfuncs is not register.renderfuncs
    assert copied_register.custom_data is not register.custom_data
    assert copied_register.custom_data["colors"] is not register.custom_data["colors"]

    # Mutating the copy must not affect the original.
    copied_register.custom_data["colors"].append("blue")
    copied_register.is_muted = False

    assert register.custom_data == {"colors": ["red", "green"]}
    assert register.is_muted is True

# Generated at 2026-10-24 20:30:15.511236
# Unit test for method mute of class Register
def test_Register_mute():
    class TestRenderType(RenderType):
        pass

    register = Register()
    rule = TestRenderType(42)

    register.set_renderfunc(TestRenderType, lambda value: f"<{value}>")
    register.example = Style(rule)

    assert register.example == "<42>"
    assert register.is_muted is False

    register.mute()

    assert register.is_muted is True
    assert register.example == ""
    assert register.example.rules == (rule,)
    assert register(42) == ""
    assert register(1, 2, 3) == ""
    assert register("example") == ""

# Generated at 2026-10-24 20:30:22.268482
# Unit test for method mute of class Register
def test_Register_mute():register = Register()

# Generated at 2026-10-24 20:30:46.950015
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:30:49.366468
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:30:51.983531
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:31:00.260447
# Unit test for constructor of class Style
def test_Style():
    rule1 = Style(value="rule1")
    rule2 = Style(value="rule2")

    style = Style(rule1, rule2, value="\x1b[1m")

    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert str(style) == "\x1b[1m"
    assert style.rules == (rule1, rule2)

    empty_style = Style(rule1)
    assert str(empty_style) == ""
    assert empty_style.rules == (rule1,)

# Generated at 2026-10-24 20:31:10.909495
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    register = Register()

    class RgbRenderType(RenderType):
        pass

    def render_rgb(red: int, green: int, blue: int) -> str:
        return f"rgb({red},{green},{blue})"

    register.renderfuncs[RgbRenderType] = render_rgb

    register.set_rgb_call(RgbRenderType)

    assert register.rgb_call is render_rgb
    assert register(10, 42, 255) == "rgb(10,42,255)"

# Generated at 2026-10-24 20:31:29.546807
# Unit test for constructor of class Register
def test_Register():
    reg = Register()

    assert isinstance(reg.renderfuncs, dict)
    assert reg.renderfuncs == {}

    assert reg.is_muted is False

    assert callable(reg.eightbit_call)
    assert reg.eightbit_call(42) == 42

    assert callable(reg.rgb_call)
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)

    # fresh register has no Style attributes
    assert reg.as_dict() == {}

    # each instance gets its own dict (no shared mutable state)
    other = Register()
    assert other.renderfuncs == {}
    assert other.renderfuncs is not reg.renderfuncs

# Generated at 2026-10-24 20:31:31.968388
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:31:34.382252
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:31:36.798307
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:31:39.214229
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:31:41.631924
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:31:44.052585
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:31:46.465991
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:31:48.881018
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:31:51.296992
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:31:53.716065
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:31:56.134344
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:31:58.551399
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:32:00.967589
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:32:03.386187
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:32:05.805477
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:32:08.223679
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:32:10.640171
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:32:13.056287
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:32:15.474005
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:32:17.889965
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:32:20.307921
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:32:22.728282
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:32:25.139828
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:32:27.556410
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:32:29.972641
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:32:32.390544
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:32:34.838839
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:32:37.225116
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:32:39.642939
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:32:42.063970
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:32:44.478198
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:32:46.895480
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:32:49.315929
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:32:51.735169
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:32:54.153303
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:32:56.572717
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:32:58.986524
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:33:01.401974
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:33:03.820308
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:33:06.236554
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:33:08.656346
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:33:11.072994
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:33:13.488821
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:33:15.905551
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:33:18.322786
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:33:20.742634
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:33:23.158976
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:33:25.575162
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:33:27.995691
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:33:30.410652
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:33:32.829247
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:33:35.246154
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:33:37.662324
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:33:40.079229
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:33:42.498226
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:33:44.911960
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:33:47.332030
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:33:49.808169
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:33:52.224066
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:34:03.577435
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:34:05.015196
# Unit test for constructor of class Register
def test_Register():
    reg = Register()

    assert isinstance(reg.renderfuncs, dict)
    assert reg.renderfuncs == {}

    assert reg.is_muted is False

    assert callable(reg.eightbit_call)
    assert reg.eightbit_call(42) == 42

    assert callable(reg.rgb_call)
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)

    # fresh register has no Style attributes
    assert reg.as_dict() == {}

    # each instance gets its own dict (no shared mutable state)
    other = Register()
    assert other.renderfuncs == {}
    assert other.renderfuncs is not reg.renderfuncs

# Generated at 2026-10-24 20:34:06.349693
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:34:15.744174
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():register = Register()

# Generated at 2026-10-24 20:34:17.163512
# Unit test for constructor of class Register
def test_Register():
    reg = Register()

    assert isinstance(reg.renderfuncs, dict)
    assert reg.renderfuncs == {}

    assert reg.is_muted is False

    assert callable(reg.eightbit_call)
    assert reg.eightbit_call(42) == 42

    assert callable(reg.rgb_call)
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)

    # fresh register has no Style attributes
    assert reg.as_dict() == {}

    # each instance gets its own dict (no shared mutable state)
    other = Register()
    assert other.renderfuncs == {}
    assert other.renderfuncs is not reg.renderfuncs

# Generated at 2026-10-24 20:34:18.524156
# Unit test for constructor of class Register
def test_Register():
    reg = Register()

    assert isinstance(reg.renderfuncs, dict)
    assert reg.renderfuncs == {}

    assert reg.is_muted is False

    assert callable(reg.eightbit_call)
    assert reg.eightbit_call(42) == 42

    assert callable(reg.rgb_call)
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)

    # fresh register has no Style attributes
    assert reg.as_dict() == {}

    # each instance gets its own dict (no shared mutable state)
    other = Register()
    assert other.renderfuncs == {}
    assert other.renderfuncs is not reg.renderfuncs

# Generated at 2026-10-24 20:34:21.042823
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:34:23.456617
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:34:25.873940
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:34:28.294676
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:34:30.712471
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:34:33.131758
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:34:35.702135
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:34:38.120122
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:34:40.536658
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:34:42.952508
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:34:45.368161
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:34:47.784560
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:34:50.200860
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:34:52.616544
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:34:55.035812
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:34:57.451912
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:34:59.867117
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:35:02.283041
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:35:04.699477
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:35:07.132664
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:35:09.578043
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:35:11.997082
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:35:14.413391
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:35:16.832222
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:35:19.248028
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:35:21.665995
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:35:24.082511
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:35:26.499848
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:35:28.915418
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:35:31.330832
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:35:33.755998
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:35:36.166442
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:35:38.585785
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:36:31.525846
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-24 20:36:33.946062
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:36:36.366933
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:36:38.784633
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:36:41.201699
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:36:43.619326
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:36:46.037457
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:37:17.400544
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-24 20:37:19.038019
# Unit test for constructor of class Register
def test_Register():
    reg = Register()

    assert isinstance(reg.renderfuncs, dict)
    assert reg.renderfuncs == {}

    assert reg.is_muted is False

    assert callable(reg.eightbit_call)
    assert reg.eightbit_call(42) == 42

    assert callable(reg.rgb_call)
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)

    # fresh register has no Style attributes
    assert reg.as_dict() == {}

    # each instance gets its own dict (no shared mutable state)
    other = Register()
    assert other.renderfuncs == {}
    assert other.renderfuncs is not reg.renderfuncs

# Generated at 2026-10-24 20:37:47.968424
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-24 20:38:12.697242
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-24 20:38:14.129528
# Unit test for constructor of class Register
def test_Register():
    reg = Register()

    assert isinstance(reg.renderfuncs, dict)
    assert reg.renderfuncs == {}

    assert reg.is_muted is False

    assert callable(reg.eightbit_call)
    assert reg.eightbit_call(42) == 42

    assert callable(reg.rgb_call)
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)

    # fresh register has no Style attributes
    assert reg.as_dict() == {}

    # each instance gets its own dict (no shared mutable state)
    other = Register()
    assert other.renderfuncs == {}
    assert other.renderfuncs is not reg.renderfuncs

# Generated at 2026-10-24 20:38:15.557859
# Unit test for constructor of class Register
def test_Register():
    reg = Register()

    assert isinstance(reg.renderfuncs, dict)
    assert reg.renderfuncs == {}

    assert reg.is_muted is False

    assert callable(reg.eightbit_call)
    assert reg.eightbit_call(42) == 42

    assert callable(reg.rgb_call)
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)

    # fresh register has no Style attributes
    assert reg.as_dict() == {}

    # each instance gets its own dict (no shared mutable state)
    other = Register()
    assert other.renderfuncs == {}
    assert other.renderfuncs is not reg.renderfuncs

# Generated at 2026-10-24 20:38:40.857607
# Unit test for method __call__ of class Register
def test_Register___call__():
    from sty import Register, Style

    # 1) Set up a register with custom render functions we can observe.
    reg = Register()
    calls = []
    reg.eightbit_call = lambda x: f"eightbit:{x}"
    reg.rgb_call = lambda r, g, b: f"rgb:{r},{g},{b}"
    reg.renderfuncs = {}

    # Attach a named style so string lookups work.
    reg.red = Style(value="RED")

    # 2) Single int argument -> eightbit_call
    assert reg(42) == "eightbit:42"

    # 3) Single string argument -> attribute lookup
    assert reg("red") == "RED"

    # 4) Three int arguments -> rgb_call
    assert reg(10, 20, 30) == "rgb:10,20,30"

    # 5) Wrong number of arguments -> empty string
    assert reg() == ""
    assert reg(1, 2) == ""
    assert reg(1, 2, 3, 4) == ""

    # 6) Muted register -> empty string regardless of input
    reg.is_muted = True
    assert reg(42) == ""
    assert reg("red") == ""
    assert reg(10, 20, 30) == ""

    # 7) Unmute -> behavior restored
    reg.is_muted = False
    assert reg(42) == "eightbit:42"
    assert reg("red") == "RED"

    # 8) Unknown string name -> AttributeError
    try:
        reg("does_not_exist")
        raised = False
    except AttributeError:
        raised = True
    assert raised

# Generated at 2026-10-24 20:38:48.220316
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-24 20:39:06.356442
# Unit test for method __call__ of class Register
def test_Register___call__():
    from sty import Register, Style

    # 1) Set up a register with custom render functions we can observe.
    reg = Register()
    calls = []
    reg.eightbit_call = lambda x: f"eightbit:{x}"
    reg.rgb_call = lambda r, g, b: f"rgb:{r},{g},{b}"
    reg.renderfuncs = {}

    # Attach a named style so string lookups work.
    reg.red = Style(value="RED")

    # 2) Single int argument -> eightbit_call
    assert reg(42) == "eightbit:42"

    # 3) Single string argument -> attribute lookup
    assert reg("red") == "RED"

    # 4) Three int arguments -> rgb_call
    assert reg(10, 20, 30) == "rgb:10,20,30"

    # 5) Wrong number of arguments -> empty string
    assert reg() == ""
    assert reg(1, 2) == ""
    assert reg(1, 2, 3, 4) == ""

    # 6) Muted register -> empty string regardless of input
    reg.is_muted = True
    assert reg(42) == ""
    assert reg("red") == ""
    assert reg(10, 20, 30) == ""

    # 7) Unmute -> behavior restored
    reg.is_muted = False
    assert reg(42) == "eightbit:42"
    assert reg("red") == "RED"

    # 8) Unknown string name -> AttributeError
    try:
        reg("does_not_exist")
        raised = False
    except AttributeError:
        raised = True
    assert raised

# Generated at 2026-10-24 20:39:12.098213
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-24 20:39:21.202476
# Unit test for method unmute of class Register
def test_Register_unmute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(
        DummyRenderType,
        lambda value: f"<style:{value}>",
    )
    register.example = Style(DummyRenderType(42))

    register.mute()
    assert register.is_muted is True
    assert register.example == ""

    register.unmute()
    assert register.is_muted is False
    assert isinstance(register.example, Style)
    assert register.example == "<style:42>"
    assert list(register.example.rules) == [DummyRenderType(42)]

# Generated at 2026-10-24 20:39:22.840756
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

# Generated at 2026-10-24 20:39:24.175345
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

# Generated at 2026-10-24 20:39:39.021485
# Unit test for method unmute of class Register
def test_Register_unmute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(
        DummyRenderType,
        lambda value: f"<rendered:{value}>",
    )
    register.example = Style(DummyRenderType("test"))

    assert register.example == "<rendered:test>"

    register.mute()
    assert register.is_muted is True
    assert register.example == ""

    register.unmute()

    assert register.is_muted is False
    assert isinstance(register.example, Style)
    assert register.example == "<rendered:test>"
    assert len(tuple(register.example.rules)) == 1
    assert isinstance(tuple(register.example.rules)[0], DummyRenderType)

# Generated at 2026-10-24 20:39:40.658823
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

# Generated at 2026-10-24 20:39:42.297191
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

# Generated at 2026-10-24 20:40:03.564831
# Unit test for method __call__ of class Register
def test_Register___call__():
    from sty import Register, Style

    # 1) Set up a register with custom render functions we can observe.
    reg = Register()
    calls = []
    reg.eightbit_call = lambda x: f"eightbit:{x}"
    reg.rgb_call = lambda r, g, b: f"rgb:{r},{g},{b}"
    reg.renderfuncs = {}

    # Attach a named style so string lookups work.
    reg.red = Style(value="RED")

    # 2) Single int argument -> eightbit_call
    assert reg(42) == "eightbit:42"

    # 3) Single string argument -> attribute lookup
    assert reg("red") == "RED"

    # 4) Three int arguments -> rgb_call
    assert reg(10, 20, 30) == "rgb:10,20,30"

    # 5) Wrong number of arguments -> empty string
    assert reg() == ""
    assert reg(1, 2) == ""
    assert reg(1, 2, 3, 4) == ""

    # 6) Muted register -> empty string regardless of input
    reg.is_muted = True
    assert reg(42) == ""
    assert reg("red") == ""
    assert reg(10, 20, 30) == ""

    # 7) Unmute -> behavior restored
    reg.is_muted = False
    assert reg(42) == "eightbit:42"
    assert reg("red") == "RED"

    # 8) Unknown string name -> AttributeError
    try:
        reg("does_not_exist")
        raised = False
    except AttributeError:
        raised = True
    assert raised

# Generated at 2026-10-24 20:40:12.915271
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()
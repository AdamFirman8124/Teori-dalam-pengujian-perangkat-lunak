

# Generated at 2026-10-24 20:20:41.661564
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    class DummyRgbRenderType(RenderType):
        pass

    register = Register()
    calls = []

    def render_rgb(r: int, g: int, b: int) -> str:
        calls.append((r, g, b))
        return f"rgb({r}, {g}, {b})"

    register.renderfuncs[DummyRgbRenderType] = render_rgb

    register.set_rgb_call(DummyRgbRenderType)

    assert register.rgb_call is render_rgb
    assert register(10, 42, 255) == "rgb(10, 42, 255)"
    assert calls == [(10, 42, 255)]

# Generated at 2026-10-24 20:20:44.078999
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 20:20:46.495533
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 20:21:04.164214
# Unit test for method __new__ of class Style
def test_Style___new__():s = Style.__new__(Style, value="\x1b[31m")

# Generated at 2026-10-24 20:21:26.939086
# Unit test for method mute of class Register
def test_Register_mute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    render = lambda *args: f"<{','.join(map(str, args))}>"

    register.set_renderfunc(DummyRenderType, render)
    register.set_eightbit_call(DummyRenderType)
    register.set_rgb_call(DummyRenderType)

    rule = DummyRenderType(7)
    register.example = Style(rule)

    # Verify normal rendering before muting.
    assert register.example == "<7>"
    assert register(42) == "<42>"
    assert register(1, 2, 3) == "<1,2,3>"
    assert register("example") == "<7>"

    register.mute()

    assert register.is_muted is True
    assert isinstance(register.example, Style)
    assert register.example == ""
    assert tuple(register.example.rules) == (rule,)

    # Every supported call form should be suppressed while muted.
    assert register(42) == ""
    assert register(1, 2, 3) == ""
    assert register("example") == ""

# Generated at 2026-10-24 20:21:29.454281
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:21:31.871897
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:21:34.292947
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 20:21:36.710462
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 20:21:39.126762
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 20:21:41.543172
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:21:43.960346
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:21:46.376092
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:21:48.792586
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:21:51.210691
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:21:53.627977
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:21:56.046972
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:21:58.461763
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:22:00.877929
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:22:03.297735
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:22:05.711416
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:22:08.129084
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:22:10.544006
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:22:12.962356
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:22:15.380435
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:22:17.797424
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:22:20.213373
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:22:22.633701
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:22:25.050150
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:22:27.464234
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:22:29.880369
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:22:32.301138
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 20:22:34.717037
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 20:22:37.134550
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 20:22:39.549509
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:22:41.968486
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:22:44.385193
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:22:46.800730
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:22:49.250373
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:22:51.637061
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:22:54.053500
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:22:56.470061
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:22:58.886588
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:23:01.306326
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:23:03.719867
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:23:06.138131
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:23:08.553029
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:23:10.973320
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:23:13.395324
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:23:15.811021
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 20:23:18.227585
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 20:23:20.647065
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 20:23:23.059959
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:23:25.479795
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:23:27.898365
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:23:30.317147
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:23:32.730231
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:23:35.150069
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:23:37.564360
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:23:39.980382
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:23:42.396137
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:23:44.814364
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:23:47.727605
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:23:50.794279
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:23:52.116010
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:23:59.803785
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:24:12.504283
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:24:32.779607
# Unit test for method mute of class Register
def test_Register_mute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(DummyRenderType, lambda code: f"<{code}>")
    register.set_eightbit_call(DummyRenderType)

    rule = DummyRenderType(31)
    register.red = Style(rule)

    assert register.is_muted is False
    assert register.red == "<31>"
    assert register(31) == "<31>"

    register.mute()

    assert register.is_muted is True
    assert isinstance(register.red, Style)
    assert register.red == ""
    assert tuple(register.red.rules) == (rule,)
    assert register(31) == ""

# Generated at 2026-10-24 20:24:40.766799
# Unit test for method mute of class Register
def test_Register_mute():register = Register()

# Generated at 2026-10-24 20:24:55.919375
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    import sys
    from unittest.mock import patch, sentinel

    register = Register()
    source_style = Style(sentinel.original_rule, value="old-rendering")

    module = sys.modules[Register.__module__]

    # An unmuted register renders and stores the flattened rules.
    with patch.object(
        module,
        "_render_rules",
        return_value=("\x1b[31m", (sentinel.flattened_rule,)),
    ) as render_rules:
        register.red = source_style

    render_rules.assert_called_once_with(register.renderfuncs, source_style.rules)
    assert isinstance(register.red, Style)
    assert str(register.red) == "\x1b[31m"
    assert register.red.rules == (sentinel.flattened_rule,)

    # A muted register preserves the original rules but stores an empty value.
    register.is_muted = True

    with patch.object(module, "_render_rules") as render_rules:
        register.muted_red = source_style

    render_rules.assert_not_called()
    assert isinstance(register.muted_red, Style)
    assert str(register.muted_red) == ""
    assert register.muted_red.rules == source_style.rules

    # Non-Style values are assigned without transformation.
    marker = object()
    register.other = marker

    assert register.other is marker

# Generated at 2026-10-24 20:25:20.802904
# Unit test for method mute of class Register
def test_Register_mute():
    register = Register()

    # Seed a rendered Style without depending on a concrete RenderType.
    original = Style(Style(), value="\x1b[31m")
    object.__setattr__(register, "example", original)

    register.eightbit_call = lambda value: f"8bit:{value}"

# Generated at 2026-10-24 20:25:23.224189
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:25:30.529871
# Unit test for method mute of class Register
def test_Register_mute():register = Register()

# Generated at 2026-10-24 20:25:40.466523
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
    assert register.example == "<rendered:test>"

# Generated at 2026-10-24 20:25:41.795892
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

# Generated at 2026-10-24 20:25:43.229908
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

# Generated at 2026-10-24 20:25:44.559630
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:25:54.495617
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:26:03.504142
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:26:06.041518
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:26:08.454413
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:26:10.874903
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:26:13.290717
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:26:15.708660
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:26:18.127290
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:26:20.547488
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:26:22.965770
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:26:25.383905
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:26:34.739549
# Unit test for method mute of class Register
def test_Register_mute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(DummyRenderType, lambda value: f"<{value}>")

    rule = DummyRenderType(42)
    register.example = Style(rule)

    assert register.example == "<42>"

    register.mute()

    assert register.is_muted is True
    assert register.example == ""
    assert tuple(register.example.rules) == (rule,)
    assert register(42) == ""
    assert register("example") == ""

# Generated at 2026-10-24 20:26:44.958221
# Unit test for method mute of class Register
def test_Register_mute():register = Register()

# Generated at 2026-10-24 20:27:04.743286
# Unit test for method unmute of class Register
def test_Register_unmute():
    register = Register()
    rule = RenderType(42)

    register.set_renderfunc(RenderType, lambda value: f"<{value}>")
    register.example = Style(rule)

    assert register.example == "<42>"

    register.mute()
    assert register.is_muted is True
    assert register.example == ""
    assert register.example.rules == (rule,)

    register.unmute()
    assert register.is_muted is False
    assert register.example == "<42>"
    assert register.example.rules == (rule,)

# Generated at 2026-10-24 20:27:07.272750
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:27:09.689761
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:27:12.106757
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:27:14.524388
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:27:16.953578
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:27:19.368177
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:27:21.782395
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:27:24.199421
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:27:29.994214
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 20:27:32.410026
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 20:27:34.826486
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 20:27:37.245947
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-24 20:27:39.662098
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-24 20:27:42.081717
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-24 20:27:44.502901
# Unit test for method set_rgb_call of class Register

# Generated at 2026-10-24 20:27:46.917822
# Unit test for method set_rgb_call of class Register

# Generated at 2026-10-24 20:27:49.337341
# Unit test for method set_rgb_call of class Register

# Generated at 2026-10-24 20:27:51.754551
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 20:27:54.174399
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 20:27:56.589411
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 20:27:59.008759
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 20:28:01.427079
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 20:28:03.844815
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 20:28:06.263662
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:28:08.679540
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:28:11.096709
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 20:28:13.516068
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:28:15.935408
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:28:18.351420
# Unit test for constructor of class Register

# Generated at 2026-10-24 20:28:20.766651
# Unit test for constructor of class Style

# Generated at 2026-10-24 20:28:23.186446
# Unit test for constructor of class Style

# Generated at 2026-10-24 20:28:25.606145
# Unit test for constructor of class Style

# Generated at 2026-10-24 20:28:28.025170
# Unit test for constructor of class Style

# Generated at 2026-10-24 20:28:30.443029
# Unit test for constructor of class Style

# Generated at 2026-10-24 20:28:32.858686
# Unit test for constructor of class Style

# Generated at 2026-10-24 20:28:35.275214
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 20:28:37.692439
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 20:28:40.118369
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 20:28:45.723062
# Unit test for method copy of class Register

# Generated at 2026-10-24 20:28:48.119852
# Unit test for method copy of class Register

# Generated at 2026-10-24 20:28:50.535703
# Unit test for method copy of class Register

# Generated at 2026-10-24 20:28:52.952020
# Unit test for method set_eightbit_call of class Register

# Generated at 2026-10-24 20:28:55.368194
# Unit test for method set_eightbit_call of class Register

# Generated at 2026-10-24 20:28:57.787285
# Unit test for method set_eightbit_call of class Register

# Generated at 2026-10-24 20:29:00.206064
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:29:02.621510
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:29:05.039100
# Unit test for method mute of class Register

# Generated at 2026-10-24 20:29:07.456018
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:29:09.871480
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:29:12.288632
# Unit test for method unmute of class Register

# Generated at 2026-10-24 20:29:14.703813
# Unit test for constructor of class Style

# Generated at 2026-10-24 20:29:17.121164
# Unit test for constructor of class Style

# Generated at 2026-10-24 20:29:19.539208
# Unit test for constructor of class Style

# Generated at 2026-10-24 20:29:38.441597
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:29:41.718187
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:29:44.483163
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 20:29:45.853976
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:29:54.110281
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 20:30:03.017442
# Unit test for method set_renderfunc of class Register
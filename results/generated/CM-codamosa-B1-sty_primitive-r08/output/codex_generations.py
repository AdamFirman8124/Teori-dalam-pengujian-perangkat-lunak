

# Generated at 2026-10-24 15:02:48.777182
# Unit test for method set_rgb_call of class Register

# Generated at 2026-10-24 15:02:51.460100
# Unit test for method set_rgb_call of class Register

# Generated at 2026-10-24 15:02:54.078413
# Unit test for method set_rgb_call of class Register

# Generated at 2026-10-24 15:02:56.635923
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:02:59.050574
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:03:01.464289
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:03:04.042581
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:03:06.459108
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:03:08.877596
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:03:11.292096
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:03:13.705567
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:03:16.128400
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:03:18.541926
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 15:03:24.998101
# Unit test for method __new__ of class Style
def test_Style___new__():from sty.primitive import Style

# Test with no rules and no explicit value: empty string, empty rules.
s0 = Style()
assert isinstance(s0, Style)
assert isinstance(s0, str)
assert str(s0) == ""
assert s0.rules == ()

# Test with rules and default empty value: str value stays "", rules are kept.
rule_a = "rule_a"
rule_b = "rule_b"
s1 = Style(rule_a, rule_b)
assert isinstance(s1, Style)
assert isinstance(s1, str)
assert str(s1) == ""
assert s1.rules == (rule_a, rule_b)

# Test with an explicit value: the string content is the value, rules are preserved.
s2 = Style("R", "G", value="\x1b[38;2;1;5;10m\x1b[1m")
assert isinstance(s2, Style)
assert isinstance(s2, str)
assert str(s2) == "\x1b[38;2;1;5;10m\x1b[1m"
assert s2 == "\x1b[38;2;1;5;10m\x1b[1m"
assert s2.rules == ("R", "G")

# Test that each instance carries its own independent rules attribute.
s3 = Style("only_rule")
assert s3.rules == ("only_rule",)
assert s1.rules == (rule_a, rule_b)

# Generated at 2026-10-24 15:03:49.777531
# Unit test for constructor of class Register
def test_Register():
    from sty import Register

    register = Register()

    # renderfuncs must start as an empty dict
    assert register.renderfuncs == {}

    # A new register is not muted
    assert register.is_muted is False

    # eightbit_call defaults to identity: returns the input unchanged
    assert register.eightbit_call(42) == 42

    # rgb_call defaults to returning its three args as a tuple
    assert register.rgb_call(10, 42, 255) == (10, 42, 255)

# Generated at 2026-10-24 15:03:52.194788
# Unit test for method mute of class Register

# Generated at 2026-10-24 15:03:54.609119
# Unit test for method mute of class Register

# Generated at 2026-10-24 15:03:57.023314
# Unit test for method mute of class Register

# Generated at 2026-10-24 15:03:59.439386
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:04:01.999408
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:04:04.413501
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:04:06.827813
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:04:09.242967
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:04:11.658825
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:04:14.073805
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 15:04:16.700256
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 15:04:19.118548
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 15:04:21.534772
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:04:23.950405
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:04:26.364947
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:04:28.779208
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:04:31.191623
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:04:55.722943
# Unit test for method __call__ of class Register
def test_Register___call__():from sty import Register, Style

# Generated at 2026-10-24 15:05:33.684870
# Unit test for method unmute of class Register

# Generated at 2026-10-24 15:05:43.442268
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

# Generated at 2026-10-24 15:05:44.874988
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

# Generated at 2026-10-24 15:06:20.308125
# Unit test for method unmute of class Register
def test_Register_unmute():
    from .rendertype import RgbFg, Sgr

    # Dummy render functions
    def render_rgb(r, g, b):
        return f"\x1b[38;2;{r};{g};{b}m"

    def render_sgr(n):
        return f"\x1b[{n}m"

    # Build a register with real renderfuncs
    r = Register()
    r.renderfuncs = {RgbFg: render_rgb, Sgr: render_sgr}
    r.is_muted = False
    r.eightbit_call = lambda x: x
    r.rgb_call = lambda a, b, c: (a, b, c)

    # Assign a style -> __setattr__ renders it immediately
    r.orange = Style(RgbFg(1, 5, 10), Sgr(1))
    expected = "\x1b[38;2;1;5;10m\x1b[1m"
    assert str(r.orange) == expected

    # Mute -> rendered value becomes "", rules are preserved
    r.mute()
    assert str(r.orange) == ""
    assert r.orange.rules == (RgbFg(1, 5, 10), Sgr(1))

    # Unmute -> styles are re-rendered from the preserved rules
    r.unmute()
    assert r.is_muted is False
    assert str(r.orange) == expected
    assert r.orange.rules == (RgbFg(1, 5, 10), Sgr(1))

# Generated at 2026-10-24 15:06:22.890924
# Unit test for method unmute of class Register

# Generated at 2026-10-24 15:06:25.303195
# Unit test for method unmute of class Register

# Generated at 2026-10-24 15:06:27.715837
# Unit test for method unmute of class Register

# Generated at 2026-10-24 15:06:30.443778
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 15:06:32.858735
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 15:06:35.273160
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 15:06:37.688522
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:06:40.099614
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:06:42.513308
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:07:26.365893
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    # 1. An empty register exports an empty dict.
    reg = Register()
    assert reg.as_dict() == {}

    # 2. Style attributes and plain strings are exported with their string values.
    reg.red = Style(value="\x1b[31m")
    reg.blue = Style(value="\x1b[34m")
    reg.plain = "hello"

    assert reg.as_dict() == {
        "red": "\x1b[31m",
        "blue": "\x1b[34m",
        "plain": "hello",
    }

    # 3. Non-string attributes are excluded (bool, dict, callables).
    result = reg.as_dict()
    assert "is_muted" not in result
    assert "renderfuncs" not in result
    assert "eightbit_call" not in result
    assert "rgb_call" not in result

    # 4. Underscore-prefixed attributes are excluded.
    reg._private = "secret"
    assert "_private" not in reg.as_dict()

    # 5. Mutting re-renders all existing styles to empty strings,
    #    and new styles set while muted are empty as well.
    reg.mute()
    reg.green = Style(value="\x1b[32m")

    muted_result = reg.as_dict()
    assert muted_result["red"] == ""
    assert muted_result["blue"] == ""
    assert muted_result["green"] == ""
    # Plain string attributes are untouched by muting.
    assert muted_result["plain"] == "hello"

# Generated at 2026-10-24 15:07:28.947108
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:07:31.361645
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:07:33.775434
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:07:36.188576
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:07:38.605058
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:07:41.018396
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:07:43.431114
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:07:45.846450
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:07:48.259055
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:07:50.673761
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:07:53.087743
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:07:55.502925
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:07:57.924224
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:08:00.330369
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:08:02.744788
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:08:05.158852
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:08:07.572518
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:08:29.432657
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():from sty.register import Register, Style

# Generated at 2026-10-24 15:08:45.892532
# Unit test for constructor of class Register
def test_Register():
    from sty import Register

    register = Register()

    # renderfuncs must start as an empty dict
    assert register.renderfuncs == {}

    # A new register is not muted
    assert register.is_muted is False

    # eightbit_call defaults to identity: returns the input unchanged
    assert register.eightbit_call(42) == 42

    # rgb_call defaults to returning its three args as a tuple
    assert register.rgb_call(10, 42, 255) == (10, 42, 255)

# Generated at 2026-10-24 15:08:48.311194
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 15:08:50.729466
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 15:08:53.139178
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 15:08:55.556809
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:08:57.970835
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:09:00.383319
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:09:02.795520
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 15:09:05.209506
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 15:09:07.619743
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 15:09:10.033179
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:09:22.761023
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():from sty.register import Register, Style

# Generated at 2026-10-24 15:09:25.776833
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    # 1. An empty register exports an empty dict.
    reg = Register()
    assert reg.as_dict() == {}

    # 2. Style attributes and plain strings are exported with their string values.
    reg.red = Style(value="\x1b[31m")
    reg.blue = Style(value="\x1b[34m")
    reg.plain = "hello"

    assert reg.as_dict() == {
        "red": "\x1b[31m",
        "blue": "\x1b[34m",
        "plain": "hello",
    }

    # 3. Non-string attributes are excluded (bool, dict, callables).
    result = reg.as_dict()
    assert "is_muted" not in result
    assert "renderfuncs" not in result
    assert "eightbit_call" not in result
    assert "rgb_call" not in result

    # 4. Underscore-prefixed attributes are excluded.
    reg._private = "secret"
    assert "_private" not in reg.as_dict()

    # 5. Mutting re-renders all existing styles to empty strings,
    #    and new styles set while muted are empty as well.
    reg.mute()
    reg.green = Style(value="\x1b[32m")

    muted_result = reg.as_dict()
    assert muted_result["red"] == ""
    assert muted_result["blue"] == ""
    assert muted_result["green"] == ""
    # Plain string attributes are untouched by muting.
    assert muted_result["plain"] == "hello"

# Generated at 2026-10-24 15:09:51.229967
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:09:53.640369
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:09:56.051164
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:09:58.464810
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:10:00.878334
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:10:03.292772
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:10:05.708561
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:10:08.120779
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:10:10.533123
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:10:12.949560
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 15:10:15.364950
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 15:10:17.778685
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 15:10:20.187096
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:10:22.603876
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:10:25.017688
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:10:27.429822
# Unit test for method copy of class Register

# Generated at 2026-10-24 15:10:29.844694
# Unit test for method copy of class Register

# Generated at 2026-10-24 15:10:32.261464
# Unit test for method copy of class Register

# Generated at 2026-10-24 15:10:34.674037
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-24 15:10:37.087909
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-24 15:10:39.497072
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-24 15:10:41.913130
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 15:10:44.323675
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 15:10:46.742183
# Unit test for method __new__ of class Style

# Generated at 2026-10-24 15:10:49.154385
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:10:51.569269
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:10:53.984688
# Unit test for constructor of class Register

# Generated at 2026-10-24 15:10:56.396114
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 15:10:58.813356
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 15:11:01.226756
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 15:11:03.645513
# Unit test for method copy of class Register

# Generated at 2026-10-24 15:11:06.062139
# Unit test for method copy of class Register

# Generated at 2026-10-24 15:11:26.823117
# Unit test for method copy of class Register
def test_Register_copy():reg = Register()

# Generated at 2026-10-24 15:11:43.534289
# Unit test for constructor of class Register
def test_Register():
    from sty import Register

    register = Register()

    # renderfuncs must start as an empty dict
    assert register.renderfuncs == {}

    # A new register is not muted
    assert register.is_muted is False

    # eightbit_call defaults to identity: returns the input unchanged
    assert register.eightbit_call(42) == 42

    # rgb_call defaults to returning its three args as a tuple
    assert register.rgb_call(10, 42, 255) == (10, 42, 255)

# Generated at 2026-10-24 15:11:45.950004
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:11:48.496852
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:11:50.916021
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:11:53.330844
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:11:55.746712
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:11:58.161472
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:12:00.575634
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:12:02.990486
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:12:05.423207
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:12:07.833112
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:12:10.243320
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:12:12.653708
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 15:12:15.069406
# Unit test for method copy of class Register

# Generated at 2026-10-24 15:12:17.480030
# Unit test for method copy of class Register

# Generated at 2026-10-24 15:12:19.896232
# Unit test for method copy of class Register

# Generated at 2026-10-24 15:12:22.307470
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:12:24.721064
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:12:27.133000
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 15:12:29.548976
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-24 15:12:31.960656
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-24 15:12:50.660479
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


# Generated at 2026-10-25 01:27:51.493748
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    register = Register()

    def render_rgb(r: int, g: int, b: int) -> str:
        return f"rgb({r},{g},{b})"

    register.renderfuncs[RenderType] = render_rgb
    register.set_rgb_call(RenderType)

    assert register.rgb_call is render_rgb
    assert register(12, 34, 56) == "rgb(12,34,56)"

# Generated at 2026-10-25 01:28:18.505043
# Unit test for method as_dict of class Register
def test_Register_as_dict():register = Register()

# Generated at 2026-10-25 01:28:54.052752
# Unit test for method as_dict of class Register

# Generated at 2026-10-25 01:29:00.606286
# Unit test for method as_dict of class Register
def test_Register_as_dict():register = Register()

# Generated at 2026-10-25 01:29:03.139233
# Unit test for method as_dict of class Register

# Generated at 2026-10-25 01:29:05.553228
# Unit test for method as_dict of class Register

# Generated at 2026-10-25 01:29:07.968230
# Unit test for method as_dict of class Register

# Generated at 2026-10-25 01:29:10.548922
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-25 01:29:13.076771
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-25 01:29:15.496849
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-25 01:29:18.603921
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:29:21.019259
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:29:23.435966
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:29:25.853370
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:29:28.272822
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:29:30.689530
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:29:33.105725
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:29:35.520091
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:29:37.935179
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:29:40.350132
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:29:42.765056
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:29:49.079891
# Unit test for constructor of class Register
def test_Register():register = Register()

# Generated at 2026-10-25 01:29:50.412240
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:29:57.045904
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 01:29:58.397364
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

# Generated at 2026-10-25 01:29:59.725953
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

# Generated at 2026-10-25 01:30:01.057803
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

# Generated at 2026-10-25 01:30:02.457573
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:30:08.605735
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 01:30:09.940724
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

# Generated at 2026-10-25 01:30:11.366237
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:30:18.005392
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 01:30:20.530995
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:30:23.051457
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:30:25.468532
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:30:28.083677
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:30:30.493170
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:30:32.908930
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:30:35.324982
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:30:37.740285
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:30:40.252674
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:30:42.670757
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:30:45.084339
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:30:47.503060
# Unit test for constructor of class Register

# Generated at 2026-10-25 01:30:49.920705
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:30:52.331694
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:30:54.745427
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:30:56.144535
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

# Generated at 2026-10-25 01:30:57.461315
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

# Generated at 2026-10-25 01:30:58.784874
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

# Generated at 2026-10-25 01:31:00.118048
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

# Generated at 2026-10-25 01:31:11.270884
# Unit test for method unmute of class Register
def test_Register_unmute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(
        DummyRenderType,
        lambda value: f"<{value}>",
    )
    register.example = Style(DummyRenderType(42))

    register.mute()
    assert register.is_muted is True
    assert register.example == ""

    register.unmute()

    assert register.is_muted is False
    assert isinstance(register.example, Style)
    assert register.example == "<42>"
    assert tuple(register.example.rules) == (DummyRenderType(42),)

# Generated at 2026-10-25 01:32:31.072445
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

# Generated at 2026-10-25 01:32:53.163903
# Unit test for method unmute of class Register
def test_Register_unmute():register = Register()

# Generated at 2026-10-25 01:32:55.583193
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:32:57.998421
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:33:00.418525
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:33:01.822524
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:33:09.135183
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 01:33:22.635186
# Unit test for method unmute of class Register
def test_Register_unmute():
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

    register.unmute()
    assert register.is_muted is False
    assert register.example == "<42>"
    assert tuple(register.example.rules) == (rule,)

# Generated at 2026-10-25 01:33:29.769465
# Unit test for method unmute of class Register
def test_Register_unmute():register = Register()
register.mute()
assert register.is_muted is True
register.unmute()
assert register.is_muted is False

# Generated at 2026-10-25 01:33:31.105030
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:33:39.939600
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 01:33:49.677678
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

    assert register.example == "<style:42>"

    register.mute()
    assert register.is_muted is True
    assert register.example == ""

    register.unmute()

    assert register.is_muted is False
    assert isinstance(register.example, Style)
    assert register.example == "<style:42>"
    assert list(register.example.rules) == [DummyRenderType(42)]

# Generated at 2026-10-25 01:33:52.200699
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:33:54.615785
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:33:57.037449
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:33:59.452620
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:34:02.051938
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:34:04.467095
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:34:06.882361
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:34:09.299775
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:34:11.713875
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:34:14.128972
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:34:16.544541
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:34:18.959476
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:34:21.373844
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:34:23.788556
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:34:26.203491
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:34:28.618475
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:34:31.032883
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:34:42.400920
# Unit test for method unmute of class Register
def test_Register_unmute():register = Register()

# Generated at 2026-10-25 01:35:15.905453
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:35:39.776976
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:36:01.984991
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:36:11.104125
# Unit test for method unmute of class Register
def test_Register_unmute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(
        DummyRenderType,
        lambda value: f"<{value}>",
    )
    register.example = Style(DummyRenderType("example"))

    assert register.example == "<example>"

    register.mute()
    assert register.is_muted is True
    assert register.example == ""

    register.unmute()
    assert register.is_muted is False
    assert isinstance(register.example, Style)
    assert register.example == "<example>"

# Generated at 2026-10-25 01:36:27.548987
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

# Generated at 2026-10-25 01:36:30.093913
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:36:32.514408
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:36:34.929956
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:36:37.341249
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:36:39.755605
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:36:42.170921
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:36:44.585199
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:36:45.969530
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:36:52.060886
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 01:36:53.391483
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 01:36:59.843932
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 01:37:13.883769
# Unit test for method unmute of class Register
def test_Register_unmute():
    class TestRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(
        TestRenderType,
        lambda value: f"\x1b[{value}m",
    )

    register.example = Style(TestRenderType(31))
    assert register.example == "\x1b[31m"

    register.mute()
    assert register.is_muted is True
    assert register.example == ""

    register.unmute()
    assert register.is_muted is False
    assert register.example == "\x1b[31m"

# Generated at 2026-10-25 01:37:26.575156
# Unit test for method unmute of class Register
def test_Register_unmute():register = Register()
register.mute()
assert register.is_muted is True

register.unmute()

assert register.is_muted is False

# Generated at 2026-10-25 01:37:38.757881
# Unit test for method unmute of class Register
def test_Register_unmute():
    class TestRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(
        TestRenderType,
        lambda value: f"<rendered:{value}>",
    )
    register.example = Style(TestRenderType("value"))

    assert register.example == "<rendered:value>"

    register.mute()
    assert register.is_muted is True
    assert register.example == ""

    register.unmute()

    assert register.is_muted is False
    assert isinstance(register.example, Style)
    assert register.example == "<rendered:value>"
    assert len(tuple(register.example.rules)) == 1
    assert isinstance(tuple(register.example.rules)[0], TestRenderType)

# Generated at 2026-10-25 01:37:41.175825
# Unit test for method unmute of class Register

# Generated at 2026-10-25 01:37:43.590266
# Unit test for method unmute of class Register
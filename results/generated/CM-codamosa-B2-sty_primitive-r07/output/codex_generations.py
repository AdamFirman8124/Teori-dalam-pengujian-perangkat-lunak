

# Generated at 2026-10-25 03:10:43.861257
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
    assert register.example.rules == (rule,)

    register.unmute()
    assert register.is_muted is False
    assert isinstance(register.example, Style)
    assert register.example == "<42>"
    assert register.example.rules == (rule,)

# Generated at 2026-10-25 03:10:57.601728
# Unit test for method unmute of class Register
def test_Register_unmute():register = Register()
register.mute()

assert register.is_muted is True
assert register(42) == ""

register.unmute()

assert register.is_muted is False
assert register(42) == 42

# Generated at 2026-10-25 03:11:00.018276
# Unit test for constructor of class Style

# Generated at 2026-10-25 03:11:02.432076
# Unit test for constructor of class Style

# Generated at 2026-10-25 03:11:04.999489
# Unit test for constructor of class Style

# Generated at 2026-10-25 03:11:07.414458
# Unit test for method copy of class Register

# Generated at 2026-10-25 03:11:09.831071
# Unit test for method copy of class Register

# Generated at 2026-10-25 03:11:12.245896
# Unit test for method copy of class Register

# Generated at 2026-10-25 03:11:14.660089
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:11:17.073822
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:11:19.489336
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:11:21.905388
# Unit test for method __new__ of class Style

# Generated at 2026-10-25 03:11:24.321580
# Unit test for method __new__ of class Style

# Generated at 2026-10-25 03:11:26.738971
# Unit test for method __new__ of class Style

# Generated at 2026-10-25 03:11:29.154776
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:11:31.571248
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:11:50.122977
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:11:51.455949
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

# Generated at 2026-10-25 03:11:52.782432
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:12:00.072165
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 03:12:02.494797
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:12:05.075310
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:12:07.489955
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:12:10.073344
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:12:12.488295
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:12:14.905223
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:12:17.319760
# Unit test for method mute of class Register

# Generated at 2026-10-25 03:12:19.734519
# Unit test for method mute of class Register

# Generated at 2026-10-25 03:12:22.150638
# Unit test for method mute of class Register

# Generated at 2026-10-25 03:12:24.565873
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:12:26.981319
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:12:29.396204
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:12:31.811391
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:12:34.228185
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:12:36.643939
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:12:39.059587
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 03:12:41.477096
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 03:12:43.892822
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 03:12:46.310509
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:12:48.725030
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:12:51.340894
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:12:52.700967
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

# Generated at 2026-10-25 03:12:54.126684
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

# Generated at 2026-10-25 03:12:55.497543
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

# Generated at 2026-10-25 03:12:56.857661
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

# Generated at 2026-10-25 03:12:58.184874
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

# Generated at 2026-10-25 03:12:59.514747
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:13:06.934252
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 03:13:08.259869
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

# Generated at 2026-10-25 03:13:10.790002
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:13:13.205846
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:13:15.620391
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:13:18.035289
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:13:20.450234
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:13:22.865762
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:13:25.282302
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:13:27.700787
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:13:30.113783
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:13:32.530294
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:13:34.939563
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:13:37.354433
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:13:39.766553
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:13:42.183830
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:13:44.596630
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:13:47.009876
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:13:49.423693
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:13:51.838371
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:13:53.591201
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:13:59.720734
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 03:14:01.054375
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

# Generated at 2026-10-25 03:14:02.408732
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

# Generated at 2026-10-25 03:14:03.761790
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

# Generated at 2026-10-25 03:14:05.096511
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

# Generated at 2026-10-25 03:14:06.530925
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

# Generated at 2026-10-25 03:14:07.870564
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:14:15.751073
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 03:14:18.279106
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:14:20.694105
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:14:23.212562
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:14:25.627213
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:14:28.042600
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:14:30.457358
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:14:33.049738
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:14:35.465992
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:14:37.883568
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:14:40.298317
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:14:42.715708
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:14:45.130062
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:14:47.544633
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:14:49.958706
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:14:52.373943
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:14:54.788740
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:14:57.203486
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:14:59.618563
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:15:02.033007
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:15:04.448932
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:15:06.863459
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:15:09.278189
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:15:11.692927
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:15:14.108518
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:15:16.527502
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:15:18.945289
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:15:21.355382
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:15:23.769818
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:15:26.184280
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:15:28.598700
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:15:31.013785
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:15:33.427578
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:15:35.841724
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:15:37.178579
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

# Generated at 2026-10-25 03:15:38.626809
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:15:46.272126
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 03:15:47.708762
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:15:53.234710
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 03:15:54.572300
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:16:01.220089
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 03:16:02.654299
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:16:08.189579
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 03:16:09.536858
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

# Generated at 2026-10-25 03:16:10.952339
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

# Generated at 2026-10-25 03:16:12.291677
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

# Generated at 2026-10-25 03:16:13.678846
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:16:21.086314
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 03:16:22.507345
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:16:30.513199
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 03:16:33.043733
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:16:35.577862
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:16:38.104989
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:16:42.621680
# Unit test for constructor of class Register

# Generated at 2026-10-25 03:16:52.046807
# Unit test for constructor of class Register
def test_Register():reg = Register()

# Generated at 2026-10-25 03:16:53.379059
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

# Generated at 2026-10-25 03:16:54.736618
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

# Generated at 2026-10-25 03:16:56.122963
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

# Generated at 2026-10-25 03:16:57.448575
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

# Generated at 2026-10-25 03:16:58.872083
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:17:03.994312
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 03:17:05.427219
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

# Generated at 2026-10-25 03:17:06.781384
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

# Generated at 2026-10-25 03:17:08.118543
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

# Generated at 2026-10-25 03:17:09.504478
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

# Generated at 2026-10-25 03:17:16.351301
# Unit test for method copy of class Register

# Generated at 2026-10-25 03:17:18.881616
# Unit test for method copy of class Register

# Generated at 2026-10-25 03:17:21.296474
# Unit test for method copy of class Register

# Generated at 2026-10-25 03:17:23.711714
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:17:26.126860
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:17:28.541809
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:17:30.956816
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-25 03:17:33.376331
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-25 03:17:35.791006
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-25 03:17:38.203306
# Unit test for method mute of class Register

# Generated at 2026-10-25 03:17:40.811922
# Unit test for method mute of class Register

# Generated at 2026-10-25 03:17:43.228564
# Unit test for method mute of class Register

# Generated at 2026-10-25 03:17:45.644900
# Unit test for method unmute of class Register

# Generated at 2026-10-25 03:17:48.058725
# Unit test for method unmute of class Register

# Generated at 2026-10-25 03:17:50.476350
# Unit test for method unmute of class Register

# Generated at 2026-10-25 03:17:52.893837
# Unit test for method as_dict of class Register

# Generated at 2026-10-25 03:17:55.309571
# Unit test for method as_dict of class Register

# Generated at 2026-10-25 03:17:57.724432
# Unit test for method as_dict of class Register

# Generated at 2026-10-25 03:18:00.138581
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:18:02.554835
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:18:04.970046
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:18:07.385129
# Unit test for method unmute of class Register

# Generated at 2026-10-25 03:18:09.801461
# Unit test for method unmute of class Register

# Generated at 2026-10-25 03:18:12.218919
# Unit test for method unmute of class Register

# Generated at 2026-10-25 03:18:14.643849
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-25 03:18:17.059204
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-25 03:18:19.475741
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-25 03:18:21.892318
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 03:18:24.307121
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 03:18:26.723043
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 03:18:40.968841
# Unit test for method copy of class Register

# Generated at 2026-10-25 03:18:43.383949
# Unit test for method copy of class Register

# Generated at 2026-10-25 03:18:59.307375
# Unit test for method copy of class Register
def test_Register_copy():orig = Register()

# Generated at 2026-10-25 03:19:00.647348
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

# Generated at 2026-10-25 03:19:02.061541
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

# Generated at 2026-10-25 03:19:03.496526
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

# Generated at 2026-10-25 03:19:40.818665
# Unit test for method as_dict of class Register

# Generated at 2026-10-25 03:19:43.235444
# Unit test for method as_dict of class Register

# Generated at 2026-10-25 03:19:45.690030
# Unit test for method as_dict of class Register

# Generated at 2026-10-25 03:19:48.077256
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:19:50.489154
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:19:52.908599
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 03:19:55.321047
# Unit test for method set_rgb_call of class Register

# Generated at 2026-10-25 03:19:57.737140
# Unit test for method set_rgb_call of class Register

# Generated at 2026-10-25 03:20:00.152292
# Unit test for method set_rgb_call of class Register

# Generated at 2026-10-25 03:20:02.565356
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-25 03:20:04.980366
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-25 03:20:07.394180
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-25 03:20:09.810979
# Unit test for method copy of class Register

# Generated at 2026-10-25 03:20:12.225646
# Unit test for method copy of class Register

# Generated at 2026-10-25 03:20:14.637251
# Unit test for method copy of class Register

# Generated at 2026-10-25 03:20:17.052498
# Unit test for method unmute of class Register

# Generated at 2026-10-25 03:20:19.469664
# Unit test for method unmute of class Register

# Generated at 2026-10-25 03:20:21.886403
# Unit test for method unmute of class Register

# Generated at 2026-10-25 03:20:45.078800
# Unit test for method copy of class Register
def test_Register_copy():reg = Register()


# Generated at 2026-10-24 07:47:52.171474
# Unit test for method mute of class Register

# Generated at 2026-10-24 07:47:54.673763
# Unit test for method mute of class Register

# Generated at 2026-10-24 07:47:57.089944
# Unit test for method mute of class Register

# Generated at 2026-10-24 07:48:14.431246
# Unit test for method __call__ of class Register
def test_Register___call__():
    class Dummy(RenderType):
        pass

    def render_dummy(*args):
        return "<dummy{!r}>".format(tuple(args))

    # Setup a register with a dummy render function.
    r = Register()
    r.renderfuncs[Dummy] = render_dummy
    r.set_eightbit_call(Dummy)
    r.set_rgb_call(Dummy)

    # Attach a named style attribute (gets rendered on assignment).
    r.orange = Style(Dummy(1, 2, 3))
    assert str(r.orange) == "<dummy(1, 2, 3)>"

    # 8bit-call: single int arg -> eightbit_call is used.
    assert r(42) == "<dummy(42,)>"

    # 24bit-call: three int args -> rgb_call is used.
    assert r(1, 2, 3) == "<dummy(1, 2, 3)>"

    # String call: returns the attribute with the matching name.
    assert r("orange") == "<dummy(1, 2, 3)>"

    # String call with a non-existing name raises AttributeError.
    try:
        r("does_not_exist")  # type: ignore
        raised = False
    except AttributeError:
        raised = True
    assert raised is True

    # Wrong number of args -> empty string.
    assert r() == ""
    assert r(1, 2) == ""
    assert r(1, 2, 3, 4) == ""

    # Muted register: every call returns an empty string.
    r.mute()
    assert r.is_muted is True
    assert r(42) == ""
    assert r(1, 2, 3) == ""
    assert r("orange") == ""

    # Muting also blanks already-rendered style attributes.
    assert str(r.orange) == ""

    # Unmuting re-renders the styles and restores normal calls.
    r.unmute()
    assert r.is_muted is False
    assert str(r.orange) == "<dummy(1, 2, 3)>"
    assert r(42) == "<dummy(42,)>"
    assert r(1, 2, 3) == "<dummy(1, 2, 3)>"
    assert r("orange") == "<dummy(1, 2, 3)>"

    # Copying a register preserves call behavior.
    r2 = r.copy()
    assert r2(42) == "<dummy(42,)>"
    assert r2(1, 2, 3) == "<dummy(1, 2, 3)>"
    assert r2("orange") == "<dummy(1, 2, 3)>"

# Generated at 2026-10-24 07:48:24.020922
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    register = Register()
    calls = []

    def render_eightbit(value: int) -> str:
        calls.append(value)
        return f"eightbit:{value}"

    register.renderfuncs[RenderType] = render_eightbit
    register.set_eightbit_call(RenderType)

    assert register.eightbit_call is render_eightbit
    assert register(42) == "eightbit:42"
    assert calls == [42]

# Generated at 2026-10-24 07:48:40.589525
# Unit test for constructor of class Style
def test_Style():
    rule_one = Style(value="rule-one")
    rule_two = Style(value="rule-two")

    style = Style(rule_one, rule_two, value="\x1b[1m")

    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert str(style) == "\x1b[1m"
    assert style.rules == (rule_one, rule_two)

    empty_style = Style()

    assert str(empty_style) == ""
    assert empty_style.rules == ()

# Generated at 2026-10-24 07:48:43.091543
# Unit test for method set_rgb_call of class Register

# Generated at 2026-10-24 07:48:45.507214
# Unit test for method set_rgb_call of class Register

# Generated at 2026-10-24 07:48:47.922327
# Unit test for method set_rgb_call of class Register

# Generated at 2026-10-24 07:48:50.335345
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:48:52.751312
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:48:55.166299
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:48:57.580363
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:48:59.994644
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:49:02.408881
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:49:23.408276
# Unit test for constructor of class Register
def test_Register():
    register = Register()

    assert register.renderfuncs == {}
    assert register.is_muted is False
    assert register.eightbit_call(42) == 42
    assert register.rgb_call(1, 2, 3) == (1, 2, 3)

# Generated at 2026-10-24 07:49:25.826986
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:49:28.241780
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:49:30.661895
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:49:33.073672
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:49:35.488875
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:49:37.904697
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:49:40.319426
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:49:42.731885
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:49:45.144698
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:49:47.558385
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:49:49.972721
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:49:52.388548
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:49:54.804402
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:49:57.217997
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:49:59.632233
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:50:02.046979
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:50:04.462999
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:50:06.878839
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:50:09.294770
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:50:11.708535
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:50:14.123532
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:50:16.537231
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:50:18.953773
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:50:25.569651
# Unit test for constructor of class Register
def test_Register():register = Register()

# Generated at 2026-10-24 07:51:00.657064
# Unit test for constructor of class Register
def test_Register():
    reg = Register()

    # instance created correctly
    assert isinstance(reg, Register)

    # __init__ defaults
    assert reg.renderfuncs == {}
    assert isinstance(reg.renderfuncs, dict)
    assert reg.is_muted is False

    # default calls defined in __init__
    assert callable(reg.eightbit_call)
    assert callable(reg.rgb_call)
    assert reg.eightbit_call(42) == 42
    assert reg.rgb_call(1, 5, 10) == (1, 5, 10)

    # each instance gets its own state - no shared mutable
    reg2 = Register()
    assert reg.renderfuncs is not reg2.renderfuncs
    assert reg.eightbit_call is not reg2.eightbit_call
    assert reg.rgb_call is not reg2.rgb_call

    # __setattr__ non-Style path used by __init__
    reg.custom_attr = "value"
    assert reg.custom_attr == "value"

# Generated at 2026-10-24 07:51:03.174532
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:51:05.690274
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:51:08.102741
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:51:10.521487
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:51:12.938150
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:51:15.353342
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:51:17.781182
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:51:20.186187
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:51:48.817239
# Unit test for method __call__ of class Register
def test_Register___call__():reg = Register()

    # Single int arg -> 8bit call (default render is identity)

# Generated at 2026-10-24 07:52:00.173967
# Unit test for method __call__ of class Register
def test_Register___call__():
    r = Register()

    # --- Case: 1 int arg -> eightbit_call ---
    r.eightbit_call = lambda x: f"eightbit:{x}"
    assert r(42) == "eightbit:42"
    assert r(42, foo="bar") == "eightbit:42"  # kwargs forwarded

    # --- Case: 1 str arg -> attribute lookup ---
    r.red = Style(value="RED")
    assert r("red") == "RED"

    # --- Case: 3 args -> rgb_call ---
    r.rgb_call = lambda x, y, z: f"rgb:{x},{y},{z}"
    assert r(10, 42, 255) == "rgb:10,42,255"
    assert r(10, 42, 255, foo="bar") == "rgb:10,42,255"  # kwargs forwarded

    # --- Case: wrong arg count -> empty string ---
    assert r() == ""
    assert r(1, 2) == ""
    assert r(1, 2, 3, 4) == ""

    # --- Case: muted register -> empty string for every call type ---
    r.mute()
    assert r(42) == ""
    assert r("red") == ""
    assert r(10, 42, 255) == ""

# Generated at 2026-10-24 07:52:02.704754
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:52:05.124375
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:52:07.534976
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:09.952094
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:12.383465
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:14.782799
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:17.200067
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:19.609771
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:22.023301
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:24.443382
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:26.857424
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:29.275164
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:52:31.689222
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:52:34.103419
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:52:36.516251
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:38.931030
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:41.351807
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:43.763046
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:46.177819
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:48.591488
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:51.008262
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:52:52.372350
# Unit test for method __call__ of class Register
def test_Register___call__():reg = Register()

    # Single int arg -> 8bit call (default render is identity)

# Generated at 2026-10-24 07:52:53.684864
# Unit test for method __call__ of class Register
def test_Register___call__():
    r = Register()

    # --- Case: 1 int arg -> eightbit_call ---
    r.eightbit_call = lambda x: f"eightbit:{x}"
    assert r(42) == "eightbit:42"
    assert r(42, foo="bar") == "eightbit:42"  # kwargs forwarded

    # --- Case: 1 str arg -> attribute lookup ---
    r.red = Style(value="RED")
    assert r("red") == "RED"

    # --- Case: 3 args -> rgb_call ---
    r.rgb_call = lambda x, y, z: f"rgb:{x},{y},{z}"
    assert r(10, 42, 255) == "rgb:10,42,255"
    assert r(10, 42, 255, foo="bar") == "rgb:10,42,255"  # kwargs forwarded

    # --- Case: wrong arg count -> empty string ---
    assert r() == ""
    assert r(1, 2) == ""
    assert r(1, 2, 3, 4) == ""

    # --- Case: muted register -> empty string for every call type ---
    r.mute()
    assert r(42) == ""
    assert r("red") == ""
    assert r(10, 42, 255) == ""

# Generated at 2026-10-24 07:52:54.995519
# Unit test for method __call__ of class Register
def test_Register___call__():reg = Register()

    # Single int arg -> 8bit call (default render is identity)

# Generated at 2026-10-24 07:53:15.458846
# Unit test for constructor of class Register
def test_Register():
    register = Register()

    assert register.renderfuncs == {}
    assert register.is_muted is False

    assert callable(register.eightbit_call)
    assert register.eightbit_call(42) == 42

    assert callable(register.rgb_call)
    assert register.rgb_call(10, 20, 30) == (10, 20, 30)

# Generated at 2026-10-24 07:53:16.766336
# Unit test for method __call__ of class Register
def test_Register___call__():
    r = Register()

    # --- Case: 1 int arg -> eightbit_call ---
    r.eightbit_call = lambda x: f"eightbit:{x}"
    assert r(42) == "eightbit:42"
    assert r(42, foo="bar") == "eightbit:42"  # kwargs forwarded

    # --- Case: 1 str arg -> attribute lookup ---
    r.red = Style(value="RED")
    assert r("red") == "RED"

    # --- Case: 3 args -> rgb_call ---
    r.rgb_call = lambda x, y, z: f"rgb:{x},{y},{z}"
    assert r(10, 42, 255) == "rgb:10,42,255"
    assert r(10, 42, 255, foo="bar") == "rgb:10,42,255"  # kwargs forwarded

    # --- Case: wrong arg count -> empty string ---
    assert r() == ""
    assert r(1, 2) == ""
    assert r(1, 2, 3, 4) == ""

    # --- Case: muted register -> empty string for every call type ---
    r.mute()
    assert r(42) == ""
    assert r("red") == ""
    assert r(10, 42, 255) == ""

# Generated at 2026-10-24 07:53:18.081810
# Unit test for method __call__ of class Register
def test_Register___call__():reg = Register()

    # Single int arg -> 8bit call (default render is identity)

# Generated at 2026-10-24 07:53:39.819716
# Unit test for constructor of class Register
def test_Register():
    register = Register()

    assert register.renderfuncs == {}
    assert register.is_muted is False

    assert callable(register.eightbit_call)
    assert register.eightbit_call(42) == 42

    assert callable(register.rgb_call)
    assert register.rgb_call(10, 42, 255) == (10, 42, 255)

# Generated at 2026-10-24 07:53:42.234368
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:53:44.649529
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:53:47.063190
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:53:49.479653
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:53:51.893715
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:53:54.308784
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:53:56.720127
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:53:59.133369
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:54:01.550213
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:54:09.924914
# Unit test for constructor of class Register
def test_Register():register = Register()


# Generated at 2026-10-24 07:54:11.249414
# Unit test for method __call__ of class Register
def test_Register___call__():
    r = Register()

    # --- Case: 1 int arg -> eightbit_call ---
    r.eightbit_call = lambda x: f"eightbit:{x}"
    assert r(42) == "eightbit:42"
    assert r(42, foo="bar") == "eightbit:42"  # kwargs forwarded

    # --- Case: 1 str arg -> attribute lookup ---
    r.red = Style(value="RED")
    assert r("red") == "RED"

    # --- Case: 3 args -> rgb_call ---
    r.rgb_call = lambda x, y, z: f"rgb:{x},{y},{z}"
    assert r(10, 42, 255) == "rgb:10,42,255"
    assert r(10, 42, 255, foo="bar") == "rgb:10,42,255"  # kwargs forwarded

    # --- Case: wrong arg count -> empty string ---
    assert r() == ""
    assert r(1, 2) == ""
    assert r(1, 2, 3, 4) == ""

    # --- Case: muted register -> empty string for every call type ---
    r.mute()
    assert r(42) == ""
    assert r("red") == ""
    assert r(10, 42, 255) == ""

# Generated at 2026-10-24 07:54:12.567132
# Unit test for method __call__ of class Register
def test_Register___call__():reg = Register()

    # Single int arg -> 8bit call (default render is identity)

# Generated at 2026-10-24 07:54:33.785074
# Unit test for constructor of class Register
def test_Register():
    register = Register()

    assert register.renderfuncs == {}
    assert register.is_muted is False

    assert callable(register.eightbit_call)
    assert register.eightbit_call(42) == 42

    assert callable(register.rgb_call)
    assert register.rgb_call(10, 42, 255) == (10, 42, 255)

# Generated at 2026-10-24 07:54:54.135438
# Unit test for constructor of class Register
def test_Register():
    register = Register()

    assert register.renderfuncs == {}
    assert register.is_muted is False

    assert callable(register.eightbit_call)
    assert register.eightbit_call(42) == 42

    assert callable(register.rgb_call)
    assert register.rgb_call(10, 20, 30) == (10, 20, 30)

# Generated at 2026-10-24 07:54:56.564192
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:54:57.907520
# Unit test for method __call__ of class Register
def test_Register___call__():reg = Register()

    # Single int arg -> 8bit call (default render is identity)

# Generated at 2026-10-24 07:54:59.224095
# Unit test for method __call__ of class Register
def test_Register___call__():
    r = Register()

    # --- Case: 1 int arg -> eightbit_call ---
    r.eightbit_call = lambda x: f"eightbit:{x}"
    assert r(42) == "eightbit:42"
    assert r(42, foo="bar") == "eightbit:42"  # kwargs forwarded

    # --- Case: 1 str arg -> attribute lookup ---
    r.red = Style(value="RED")
    assert r("red") == "RED"

    # --- Case: 3 args -> rgb_call ---
    r.rgb_call = lambda x, y, z: f"rgb:{x},{y},{z}"
    assert r(10, 42, 255) == "rgb:10,42,255"
    assert r(10, 42, 255, foo="bar") == "rgb:10,42,255"  # kwargs forwarded

    # --- Case: wrong arg count -> empty string ---
    assert r() == ""
    assert r(1, 2) == ""
    assert r(1, 2, 3, 4) == ""

    # --- Case: muted register -> empty string for every call type ---
    r.mute()
    assert r(42) == ""
    assert r("red") == ""
    assert r(10, 42, 255) == ""

# Generated at 2026-10-24 07:55:00.562590
# Unit test for method __call__ of class Register
def test_Register___call__():reg = Register()

    # Single int arg -> 8bit call (default render is identity)

# Generated at 2026-10-24 07:55:01.888081
# Unit test for method __call__ of class Register
def test_Register___call__():
    r = Register()

    # --- Case: 1 int arg -> eightbit_call ---
    r.eightbit_call = lambda x: f"eightbit:{x}"
    assert r(42) == "eightbit:42"
    assert r(42, foo="bar") == "eightbit:42"  # kwargs forwarded

    # --- Case: 1 str arg -> attribute lookup ---
    r.red = Style(value="RED")
    assert r("red") == "RED"

    # --- Case: 3 args -> rgb_call ---
    r.rgb_call = lambda x, y, z: f"rgb:{x},{y},{z}"
    assert r(10, 42, 255) == "rgb:10,42,255"
    assert r(10, 42, 255, foo="bar") == "rgb:10,42,255"  # kwargs forwarded

    # --- Case: wrong arg count -> empty string ---
    assert r() == ""
    assert r(1, 2) == ""
    assert r(1, 2, 3, 4) == ""

    # --- Case: muted register -> empty string for every call type ---
    r.mute()
    assert r(42) == ""
    assert r("red") == ""
    assert r(10, 42, 255) == ""

# Generated at 2026-10-24 07:55:03.212694
# Unit test for method __call__ of class Register
def test_Register___call__():reg = Register()

    # Single int arg -> 8bit call (default render is identity)

# Generated at 2026-10-24 07:55:23.735498
# Unit test for constructor of class Register
def test_Register():
    register = Register()

    assert register.renderfuncs == {}
    assert register.is_muted is False

    assert callable(register.eightbit_call)
    assert register.eightbit_call(42) == 42

    assert callable(register.rgb_call)
    assert register.rgb_call(1, 2, 3) == (1, 2, 3)

# Generated at 2026-10-24 07:55:40.242566
# Unit test for constructor of class Register
def test_Register():
    reg = Register()

    # instance created correctly
    assert isinstance(reg, Register)

    # __init__ defaults
    assert reg.renderfuncs == {}
    assert isinstance(reg.renderfuncs, dict)
    assert reg.is_muted is False

    # default calls defined in __init__
    assert callable(reg.eightbit_call)
    assert callable(reg.rgb_call)
    assert reg.eightbit_call(42) == 42
    assert reg.rgb_call(1, 5, 10) == (1, 5, 10)

    # each instance gets its own state - no shared mutable
    reg2 = Register()
    assert reg.renderfuncs is not reg2.renderfuncs
    assert reg.eightbit_call is not reg2.eightbit_call
    assert reg.rgb_call is not reg2.rgb_call

    # __setattr__ non-Style path used by __init__
    reg.custom_attr = "value"
    assert reg.custom_attr == "value"

# Generated at 2026-10-24 07:55:42.661039
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:55:45.186953
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:55:47.603386
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:55:50.186688
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:55:52.600924
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:55:55.018034
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:55:57.437246
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:55:59.855182
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:02.269467
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:04.684342
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:07.094286
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:09.510839
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:11.934515
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:14.351491
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:16.766907
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:19.189070
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:21.596385
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:24.010936
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:26.429519
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:56:28.848178
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:56:31.263335
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:56:33.697537
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:36.112262
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:38.529780
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:40.945505
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:43.362872
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:45.774394
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:48.188750
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:50.603613
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:53.018498
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:55.435735
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:57.856565
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:00.268451
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:03.779224
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:06.191556
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:08.610643
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:11.030556
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:57:13.444745
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:57:15.864934
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:57:18.282997
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:20.701805
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:23.116967
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:25.531177
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:57:27.945696
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:57:30.362068
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:57:47.015201
# Unit test for constructor of class Register
def test_Register():
    reg = Register()

    # instance created correctly
    assert isinstance(reg, Register)

    # __init__ defaults
    assert reg.renderfuncs == {}
    assert isinstance(reg.renderfuncs, dict)
    assert reg.is_muted is False

    # default calls defined in __init__
    assert callable(reg.eightbit_call)
    assert callable(reg.rgb_call)
    assert reg.eightbit_call(42) == 42
    assert reg.rgb_call(1, 5, 10) == (1, 5, 10)

    # each instance gets its own state - no shared mutable
    reg2 = Register()
    assert reg.renderfuncs is not reg2.renderfuncs
    assert reg.eightbit_call is not reg2.eightbit_call
    assert reg.rgb_call is not reg2.rgb_call

    # __setattr__ non-Style path used by __init__
    reg.custom_attr = "value"
    assert reg.custom_attr == "value"
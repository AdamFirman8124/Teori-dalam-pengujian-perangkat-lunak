

# Generated at 2026-10-24 07:51:07.264128
# Unit test for method unmute of class Register

# Generated at 2026-10-24 07:51:09.675849
# Unit test for method unmute of class Register

# Generated at 2026-10-24 07:51:12.091288
# Unit test for method unmute of class Register

# Generated at 2026-10-24 07:51:14.504672
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:51:16.920209
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:51:19.333594
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:51:47.792847
# Unit test for constructor of class Style
def test_Style():rule1 = object()

# Generated at 2026-10-24 07:51:57.220525
# Unit test for method unmute of class Register
def test_Register_unmute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(DummyRenderType, lambda value: f"<{value}>")
    register.example = Style(DummyRenderType(42))

    assert register.example == "<42>"

    register.mute()
    assert register.is_muted is True
    assert register.example == ""

    register.unmute()
    assert register.is_muted is False
    assert register.example == "<42>"
    assert register("example") == "<42>"

# Generated at 2026-10-24 07:51:59.748238
# Unit test for method unmute of class Register

# Generated at 2026-10-24 07:52:02.291378
# Unit test for method unmute of class Register

# Generated at 2026-10-24 07:52:04.791913
# Unit test for method copy of class Register

# Generated at 2026-10-24 07:52:07.328887
# Unit test for method copy of class Register

# Generated at 2026-10-24 07:52:09.707408
# Unit test for method copy of class Register

# Generated at 2026-10-24 07:52:12.122427
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:52:14.537652
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:52:17.166606
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:52:19.577957
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:21.993527
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:24.410570
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:26.834042
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 07:52:29.241790
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 07:52:31.656993
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 07:52:34.069183
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:36.484658
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:38.897334
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:52:41.317712
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 07:52:43.731460
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 07:52:46.143621
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 07:52:48.567742
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 07:52:50.982215
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 07:53:01.214521
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 07:53:34.533514
# Unit test for constructor of class Register
def test_Register():import pytest

from sty.primitive import Register


def test_register_init_defaults():
    reg = Register()
    assert reg.renderfuncs == {}
    assert reg.is_muted is False


def test_register_init_eightbit_call_is_identity():
    reg = Register()
    assert reg.eightbit_call(5) == 5
    assert reg.eightbit_call(0) == 0
    assert reg.eightbit_call(255) == 255


def test_register_init_rgb_call_is_identity():
    reg = Register()
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)
    assert reg.rgb_call(0, 0, 0) == (0, 0, 0)


def test_register_init_is_empty_and_callable():
    reg = Register()
    assert reg.as_dict() == {}
    # Direct calls fall through to the identity defaults, not ""
    assert reg(42) == 42
    assert reg(1, 2, 3) == (1, 2, 3)


def test_register_init_instances_are_independent():
    a, b = Register(), Register()
    a.renderfuncs["x"] = lambda *args: ""
    a.is_muted = True
    assert b.renderfuncs == {}
    assert b.is_muted is False

# Generated at 2026-10-24 07:53:37.042718
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:53:39.459316
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:53:41.872227
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:53:44.368769
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 07:53:46.783757
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 07:53:49.200326
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 07:53:51.612284
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:53:54.025751
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:53:56.438936
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:53:58.853028
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:54:01.268347
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:54:08.080935
# Unit test for constructor of class Register
def test_Register():register = Register()

# Generated at 2026-10-24 07:54:25.230922
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    reg = DummyRegister()

    # 1. Initial state: style rendered with the original func
    assert str(reg.blue) == "<dummy:1>"
    assert reg.blue.rules[0].args == (1,)

    # 2. Replace the renderfunc for Dummy
    reg.set_renderfunc(Dummy, lambda *args: "<new:%d>" % (args[0] * 10))

    # 3. Existing style attributes are re-rendered with the new func
    assert str(reg.blue) == "<new:10>"

    # 4. Rules are preserved through re-rendering
    assert isinstance(reg.blue.rules[0], Dummy)
    assert reg.blue.rules[0].args == (1,)

    # 5. Non-Style attributes are left untouched
    assert reg.not_a_style == "plain string"

# Generated at 2026-10-24 07:54:26.545607
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    reg = DummyRegister()

    # 1. Initial state: style rendered with the original func
    assert str(reg.blue) == "<dummy:1>"
    assert reg.blue.rules[0].args == (1,)

    # 2. Replace the renderfunc for Dummy
    reg.set_renderfunc(Dummy, lambda *args: "<new:%d>" % (args[0] * 10))

    # 3. Existing style attributes are re-rendered with the new func
    assert str(reg.blue) == "<new:10>"

    # 4. Rules are preserved through re-rendering
    assert isinstance(reg.blue.rules[0], Dummy)
    assert reg.blue.rules[0].args == (1,)

    # 5. Non-Style attributes are left untouched
    assert reg.not_a_style == "plain string"

# Generated at 2026-10-24 07:54:47.392196
# Unit test for constructor of class Register
def test_Register():
    register = Register()

    assert register.renderfuncs == {}
    assert register.is_muted is False

    assert callable(register.eightbit_call)
    assert register.eightbit_call(42) == 42

    assert callable(register.rgb_call)
    assert register.rgb_call(1, 2, 3) == (1, 2, 3)

# Generated at 2026-10-24 07:54:49.811349
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:54:52.231661
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:54:54.752018
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:54:57.296284
# Unit test for constructor of class Register
def test_Register():register = Register()


# Generated at 2026-10-24 07:54:58.660692
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

# Generated at 2026-10-24 07:54:59.968979
# Unit test for method __call__ of class Register
def test_Register___call__():reg = Register()

    # Single int arg -> 8bit call (default render is identity)

# Generated at 2026-10-24 07:55:01.284722
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

# Generated at 2026-10-24 07:55:02.602856
# Unit test for method __call__ of class Register
def test_Register___call__():reg = Register()

    # Single int arg -> 8bit call (default render is identity)

# Generated at 2026-10-24 07:55:03.943609
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

# Generated at 2026-10-24 07:55:05.343674
# Unit test for method __call__ of class Register
def test_Register___call__():reg = Register()

    # Single int arg -> 8bit call (default render is identity)

# Generated at 2026-10-24 07:55:06.678369
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    reg = DummyRegister()

    # 1. Initial state: style rendered with the original func
    assert str(reg.blue) == "<dummy:1>"
    assert reg.blue.rules[0].args == (1,)

    # 2. Replace the renderfunc for Dummy
    reg.set_renderfunc(Dummy, lambda *args: "<new:%d>" % (args[0] * 10))

    # 3. Existing style attributes are re-rendered with the new func
    assert str(reg.blue) == "<new:10>"

    # 4. Rules are preserved through re-rendering
    assert isinstance(reg.blue.rules[0], Dummy)
    assert reg.blue.rules[0].args == (1,)

    # 5. Non-Style attributes are left untouched
    assert reg.not_a_style == "plain string"

# Generated at 2026-10-24 07:55:23.159257
# Unit test for constructor of class Register
def test_Register():import pytest

from sty.primitive import Register


def test_register_init_defaults():
    reg = Register()
    assert reg.renderfuncs == {}
    assert reg.is_muted is False


def test_register_init_eightbit_call_is_identity():
    reg = Register()
    assert reg.eightbit_call(5) == 5
    assert reg.eightbit_call(0) == 0
    assert reg.eightbit_call(255) == 255


def test_register_init_rgb_call_is_identity():
    reg = Register()
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)
    assert reg.rgb_call(0, 0, 0) == (0, 0, 0)


def test_register_init_is_empty_and_callable():
    reg = Register()
    assert reg.as_dict() == {}
    # Direct calls fall through to the identity defaults, not ""
    assert reg(42) == 42
    assert reg(1, 2, 3) == (1, 2, 3)


def test_register_init_instances_are_independent():
    a, b = Register(), Register()
    a.renderfuncs["x"] = lambda *args: ""
    a.is_muted = True
    assert b.renderfuncs == {}
    assert b.is_muted is False

# Generated at 2026-10-24 07:55:24.480602
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

# Generated at 2026-10-24 07:55:25.793572
# Unit test for method __call__ of class Register
def test_Register___call__():reg = Register()

    # Single int arg -> 8bit call (default render is identity)

# Generated at 2026-10-24 07:55:27.121242
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

# Generated at 2026-10-24 07:55:28.459137
# Unit test for method __call__ of class Register
def test_Register___call__():reg = Register()

    # Single int arg -> 8bit call (default render is identity)

# Generated at 2026-10-24 07:55:44.962431
# Unit test for constructor of class Register
def test_Register():import pytest

from sty.primitive import Register


def test_register_init_defaults():
    reg = Register()
    assert reg.renderfuncs == {}
    assert reg.is_muted is False


def test_register_init_eightbit_call_is_identity():
    reg = Register()
    assert reg.eightbit_call(5) == 5
    assert reg.eightbit_call(0) == 0
    assert reg.eightbit_call(255) == 255


def test_register_init_rgb_call_is_identity():
    reg = Register()
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)
    assert reg.rgb_call(0, 0, 0) == (0, 0, 0)


def test_register_init_is_empty_and_callable():
    reg = Register()
    assert reg.as_dict() == {}
    # Direct calls fall through to the identity defaults, not ""
    assert reg(42) == 42
    assert reg(1, 2, 3) == (1, 2, 3)


def test_register_init_instances_are_independent():
    a, b = Register(), Register()
    a.renderfuncs["x"] = lambda *args: ""
    a.is_muted = True
    assert b.renderfuncs == {}
    assert b.is_muted is False

# Generated at 2026-10-24 07:55:47.632216
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:55:50.039985
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:55:52.454516
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:55:54.872950
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:55:57.423168
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:55:59.839537
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:02.257761
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:56:04.670590
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:56:07.084571
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:56:09.501053
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:11.914679
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:14.332422
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:16.754564
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:19.172236
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:21.585832
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:23.998355
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:26.414631
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:28.831474
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:31.252273
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:33.664200
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:36.078422
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:38.491728
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:40.909964
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:43.328981
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:45.744141
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:48.158416
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:50.574063
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:52.990940
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:55.407528
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:56:57.823055
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:00.236205
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:02.649378
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:05.063441
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:07.480105
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:57:09.903052
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:57:12.317047
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:57:14.734149
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:17.156575
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:19.577748
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:22.001781
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:24.416179
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:26.829007
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:29.242103
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:57:36.071859
# Unit test for constructor of class Register
def test_Register():register = Register()

# Generated at 2026-10-24 07:57:57.054011
# Unit test for constructor of class Register
def test_Register():
    register = Register()

    assert register.renderfuncs == {}
    assert register.is_muted is False
    assert callable(register.eightbit_call)
    assert callable(register.rgb_call)

    assert register.eightbit_call(42) == 42
    assert register.rgb_call(10, 20, 30) == (10, 20, 30)

# Generated at 2026-10-24 07:57:58.373214
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

# Generated at 2026-10-24 07:57:59.815741
# Unit test for method __call__ of class Register
def test_Register___call__():reg = Register()

    # Single int arg -> 8bit call (default render is identity)

# Generated at 2026-10-24 07:58:01.145485
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

# Generated at 2026-10-24 07:58:02.499075
# Unit test for method __call__ of class Register
def test_Register___call__():reg = Register()

    # Single int arg -> 8bit call (default render is identity)

# Generated at 2026-10-24 07:58:24.394355
# Unit test for constructor of class Register
def test_Register():
    register = Register()

    assert register.renderfuncs == {}
    assert register.is_muted is False
    assert callable(register.eightbit_call)
    assert callable(register.rgb_call)

    assert register.eightbit_call(42) == 42
    assert register.rgb_call(10, 20, 30) == (10, 20, 30)

# Generated at 2026-10-24 07:58:25.700606
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

# Generated at 2026-10-24 07:58:28.410885
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:58:31.018669
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 07:58:33.440553
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:58:35.854577
# Unit test for constructor of class Register

# Generated at 2026-10-24 07:58:48.321200
# Unit test for constructor of class Register
def test_Register():from sty.register import Register


# Generated at 2026-10-24 07:59:04.802400
# Unit test for constructor of class Register
def test_Register():import pytest

from sty.primitive import Register


def test_register_init_defaults():
    reg = Register()
    assert reg.renderfuncs == {}
    assert reg.is_muted is False


def test_register_init_eightbit_call_is_identity():
    reg = Register()
    assert reg.eightbit_call(5) == 5
    assert reg.eightbit_call(0) == 0
    assert reg.eightbit_call(255) == 255


def test_register_init_rgb_call_is_identity():
    reg = Register()
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)
    assert reg.rgb_call(0, 0, 0) == (0, 0, 0)


def test_register_init_is_empty_and_callable():
    reg = Register()
    assert reg.as_dict() == {}
    # Direct calls fall through to the identity defaults, not ""
    assert reg(42) == 42
    assert reg(1, 2, 3) == (1, 2, 3)


def test_register_init_instances_are_independent():
    a, b = Register(), Register()
    a.renderfuncs["x"] = lambda *args: ""
    a.is_muted = True
    assert b.renderfuncs == {}
    assert b.is_muted is False

# Generated at 2026-10-24 07:59:21.430087
# Unit test for constructor of class Register
def test_Register():import pytest

from sty.primitive import Register


def test_register_init_defaults():
    reg = Register()
    assert reg.renderfuncs == {}
    assert reg.is_muted is False


def test_register_init_eightbit_call_is_identity():
    reg = Register()
    assert reg.eightbit_call(5) == 5
    assert reg.eightbit_call(0) == 0
    assert reg.eightbit_call(255) == 255


def test_register_init_rgb_call_is_identity():
    reg = Register()
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)
    assert reg.rgb_call(0, 0, 0) == (0, 0, 0)


def test_register_init_is_empty_and_callable():
    reg = Register()
    assert reg.as_dict() == {}
    # Direct calls fall through to the identity defaults, not ""
    assert reg(42) == 42
    assert reg(1, 2, 3) == (1, 2, 3)


def test_register_init_instances_are_independent():
    a, b = Register(), Register()
    a.renderfuncs["x"] = lambda *args: ""
    a.is_muted = True
    assert b.renderfuncs == {}
    assert b.is_muted is False

# Generated at 2026-10-24 07:59:38.007549
# Unit test for constructor of class Register
def test_Register():import pytest

from sty.primitive import Register


def test_register_init_defaults():
    reg = Register()
    assert reg.renderfuncs == {}
    assert reg.is_muted is False


def test_register_init_eightbit_call_is_identity():
    reg = Register()
    assert reg.eightbit_call(5) == 5
    assert reg.eightbit_call(0) == 0
    assert reg.eightbit_call(255) == 255


def test_register_init_rgb_call_is_identity():
    reg = Register()
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)
    assert reg.rgb_call(0, 0, 0) == (0, 0, 0)


def test_register_init_is_empty_and_callable():
    reg = Register()
    assert reg.as_dict() == {}
    # Direct calls fall through to the identity defaults, not ""
    assert reg(42) == 42
    assert reg(1, 2, 3) == (1, 2, 3)


def test_register_init_instances_are_independent():
    a, b = Register(), Register()
    a.renderfuncs["x"] = lambda *args: ""
    a.is_muted = True
    assert b.renderfuncs == {}
    assert b.is_muted is False

# Generated at 2026-10-24 07:59:54.505736
# Unit test for constructor of class Register
def test_Register():import pytest

from sty.primitive import Register


def test_register_init_defaults():
    reg = Register()
    assert reg.renderfuncs == {}
    assert reg.is_muted is False


def test_register_init_eightbit_call_is_identity():
    reg = Register()
    assert reg.eightbit_call(5) == 5
    assert reg.eightbit_call(0) == 0
    assert reg.eightbit_call(255) == 255


def test_register_init_rgb_call_is_identity():
    reg = Register()
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)
    assert reg.rgb_call(0, 0, 0) == (0, 0, 0)


def test_register_init_is_empty_and_callable():
    reg = Register()
    assert reg.as_dict() == {}
    # Direct calls fall through to the identity defaults, not ""
    assert reg(42) == 42
    assert reg(1, 2, 3) == (1, 2, 3)


def test_register_init_instances_are_independent():
    a, b = Register(), Register()
    a.renderfuncs["x"] = lambda *args: ""
    a.is_muted = True
    assert b.renderfuncs == {}
    assert b.is_muted is False

# Generated at 2026-10-24 08:00:10.924610
# Unit test for constructor of class Register
def test_Register():import pytest

from sty.primitive import Register


def test_register_init_defaults():
    reg = Register()
    assert reg.renderfuncs == {}
    assert reg.is_muted is False


def test_register_init_eightbit_call_is_identity():
    reg = Register()
    assert reg.eightbit_call(5) == 5
    assert reg.eightbit_call(0) == 0
    assert reg.eightbit_call(255) == 255


def test_register_init_rgb_call_is_identity():
    reg = Register()
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)
    assert reg.rgb_call(0, 0, 0) == (0, 0, 0)


def test_register_init_is_empty_and_callable():
    reg = Register()
    assert reg.as_dict() == {}
    # Direct calls fall through to the identity defaults, not ""
    assert reg(42) == 42
    assert reg(1, 2, 3) == (1, 2, 3)


def test_register_init_instances_are_independent():
    a, b = Register(), Register()
    a.renderfuncs["x"] = lambda *args: ""
    a.is_muted = True
    assert b.renderfuncs == {}
    assert b.is_muted is False

# Generated at 2026-10-24 08:00:12.371157
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

# Generated at 2026-10-24 08:00:13.690366
# Unit test for method __call__ of class Register
def test_Register___call__():reg = Register()

    # Single int arg -> 8bit call (default render is identity)

# Generated at 2026-10-24 08:00:35.715482
# Unit test for constructor of class Register
def test_Register():
    register = Register()

    assert register.renderfuncs == {}
    assert register.is_muted is False
    assert callable(register.eightbit_call)
    assert callable(register.rgb_call)

    assert register.eightbit_call(42) == 42
    assert register.rgb_call(10, 20, 30) == (10, 20, 30)

# Generated at 2026-10-24 08:00:38.230070
# Unit test for constructor of class Register
def test_Register():register = Register()


# Generated at 2026-10-24 08:00:54.600836
# Unit test for constructor of class Register
def test_Register():import pytest

from sty.primitive import Register


def test_register_init_defaults():
    reg = Register()
    assert reg.renderfuncs == {}
    assert reg.is_muted is False


def test_register_init_eightbit_call_is_identity():
    reg = Register()
    assert reg.eightbit_call(5) == 5
    assert reg.eightbit_call(0) == 0
    assert reg.eightbit_call(255) == 255


def test_register_init_rgb_call_is_identity():
    reg = Register()
    assert reg.rgb_call(1, 2, 3) == (1, 2, 3)
    assert reg.rgb_call(0, 0, 0) == (0, 0, 0)


def test_register_init_is_empty_and_callable():
    reg = Register()
    assert reg.as_dict() == {}
    # Direct calls fall through to the identity defaults, not ""
    assert reg(42) == 42
    assert reg(1, 2, 3) == (1, 2, 3)


def test_register_init_instances_are_independent():
    a, b = Register(), Register()
    a.renderfuncs["x"] = lambda *args: ""
    a.is_muted = True
    assert b.renderfuncs == {}
    assert b.is_muted is False

# Generated at 2026-10-24 08:01:17.251172
# Unit test for constructor of class Register
def test_Register():
    register = Register()

    assert register.renderfuncs == {}
    assert register.is_muted is False

    # Verify the default call handlers.
    assert register.eightbit_call(42) == 42
    assert register.rgb_call(10, 20, 30) == (10, 20, 30)

    # Verify Register.__call__ delegates to the default handlers.
    assert register(42) == 42
    assert register(10, 20, 30) == (10, 20, 30)

    # Each instance should have its own render-function registry.
    other_register = Register()
    assert register.renderfuncs is not other_register.renderfuncs
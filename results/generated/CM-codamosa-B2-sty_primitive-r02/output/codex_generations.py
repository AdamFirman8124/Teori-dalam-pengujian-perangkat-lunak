

# Generated at 2026-10-25 04:39:18.580693
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    from typing import Tuple

    class Dummy(RenderType):
        args: Tuple[int, ...]

    old_render = lambda *args: f"\x1b[{args[0]}m"
    new_render = lambda *args: f"<{args[0]}>"

    # --- Case 1: replaces the renderfunc in the registry ---
    reg = Register()
    reg.renderfuncs = {Dummy: old_render}
    reg.set_renderfunc(Dummy, new_render)
    assert reg.renderfuncs[Dummy] is new_render

    # --- Case 2: re-renders existing Style attributes with the new func ---
    reg2 = Register()
    reg2.renderfuncs = {Dummy: old_render}
    reg2.red = Style(Dummy(31))
    assert str(reg2.red) == "\x1b[31m"  # rendered with old func

    reg2.set_renderfunc(Dummy, new_render)
    assert str(reg2.red) == "<31>"      # re-rendered with new func

    # --- Case 3: rules are preserved after re-render (can re-render again) ---
    assert isinstance(reg2.red.rules[0], Dummy)
    reg2.set_renderfunc(Dummy, old_render)
    assert str(reg2.red) == "\x1b[31m"

# Generated at 2026-10-25 04:39:26.264635
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():register = Register()

# Generated at 2026-10-25 04:39:47.369699
# Unit test for method mute of class Register
def test_Register_mute():register = Register()

# Generated at 2026-10-25 04:39:48.694148
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    from typing import Tuple

    class Dummy(RenderType):
        args: Tuple[int, ...]

    old_render = lambda *args: f"\x1b[{args[0]}m"
    new_render = lambda *args: f"<{args[0]}>"

    # --- Case 1: replaces the renderfunc in the registry ---
    reg = Register()
    reg.renderfuncs = {Dummy: old_render}
    reg.set_renderfunc(Dummy, new_render)
    assert reg.renderfuncs[Dummy] is new_render

    # --- Case 2: re-renders existing Style attributes with the new func ---
    reg2 = Register()
    reg2.renderfuncs = {Dummy: old_render}
    reg2.red = Style(Dummy(31))
    assert str(reg2.red) == "\x1b[31m"  # rendered with old func

    reg2.set_renderfunc(Dummy, new_render)
    assert str(reg2.red) == "<31>"      # re-rendered with new func

    # --- Case 3: rules are preserved after re-render (can re-render again) ---
    assert isinstance(reg2.red.rules[0], Dummy)
    reg2.set_renderfunc(Dummy, old_render)
    assert str(reg2.red) == "\x1b[31m"

# Generated at 2026-10-25 04:40:02.292706
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:40:12.327776
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():register = Register()


# Generated at 2026-10-25 04:40:13.695421
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

# Generated at 2026-10-25 04:40:21.648027
# Unit test for method __new__ of class Style
def test_Style___new__():
    rule_1 = Style(value="rule-1")
    rule_2 = Style(value="rule-2")

    style = Style(rule_1, rule_2, value="\x1b[1m")

    assert isinstance(style, Style)
    assert isinstance(style, str)
    assert str(style) == "\x1b[1m"
    assert style.rules == (rule_1, rule_2)
    assert style.rules[0] is rule_1
    assert style.rules[1] is rule_2

# Generated at 2026-10-25 04:40:55.339139
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 04:41:05.995896
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():register = Register()

# Generated at 2026-10-25 04:41:07.428159
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

# Generated at 2026-10-25 04:41:08.854722
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

# Generated at 2026-10-25 04:41:10.289170
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

# Generated at 2026-10-25 04:41:11.627378
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

# Generated at 2026-10-25 04:41:13.051641
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

# Generated at 2026-10-25 04:41:14.486112
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

# Generated at 2026-10-25 04:41:24.213392
# Unit test for method unmute of class Register
def test_Register_unmute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(DummyRenderType, lambda value: f"<{value}>")
    register.example = Style(DummyRenderType("styled"))

    assert register.example == "<styled>"

    register.mute()
    assert register.is_muted is True
    assert register.example == ""

    register.unmute()
    assert register.is_muted is False
    assert register.example == "<styled>"

# Generated at 2026-10-25 04:41:26.630828
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:41:29.227062
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:41:30.601116
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 04:41:37.128811
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 04:41:38.552711
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 04:41:45.824653
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 04:41:47.161295
# Unit test for method __call__ of class Register

# Generated at 2026-10-25 04:41:54.217270
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-25 04:41:55.548573
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

# Generated at 2026-10-25 04:41:56.982606
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

# Generated at 2026-10-25 04:41:58.319401
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

# Generated at 2026-10-25 04:41:59.654314
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

# Generated at 2026-10-25 04:42:01.004616
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    from typing import Tuple

    class Dummy(RenderType):
        args: Tuple[int, ...]

    old_render = lambda *args: f"\x1b[{args[0]}m"
    new_render = lambda *args: f"<{args[0]}>"

    # --- Case 1: replaces the renderfunc in the registry ---
    reg = Register()
    reg.renderfuncs = {Dummy: old_render}
    reg.set_renderfunc(Dummy, new_render)
    assert reg.renderfuncs[Dummy] is new_render

    # --- Case 2: re-renders existing Style attributes with the new func ---
    reg2 = Register()
    reg2.renderfuncs = {Dummy: old_render}
    reg2.red = Style(Dummy(31))
    assert str(reg2.red) == "\x1b[31m"  # rendered with old func

    reg2.set_renderfunc(Dummy, new_render)
    assert str(reg2.red) == "<31>"      # re-rendered with new func

    # --- Case 3: rules are preserved after re-render (can re-render again) ---
    assert isinstance(reg2.red.rules[0], Dummy)
    reg2.set_renderfunc(Dummy, old_render)
    assert str(reg2.red) == "\x1b[31m"

# Generated at 2026-10-25 04:42:11.090548
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():register = Register()

# Generated at 2026-10-25 04:42:13.512322
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 04:42:15.925773
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 04:42:18.340977
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 04:42:20.919527
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:42:23.335085
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:42:25.749896
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:42:28.164506
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:42:30.583901
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:42:32.997019
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:42:35.411082
# Unit test for method mute of class Register

# Generated at 2026-10-25 04:42:37.825748
# Unit test for method mute of class Register

# Generated at 2026-10-25 04:42:39.179045
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

# Generated at 2026-10-25 04:42:54.837059
# Unit test for method as_dict of class Register
def test_Register_as_dict():register = Register()

# Generated at 2026-10-25 04:43:10.812631
# Unit test for method unmute of class Register
def test_Register_unmute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(
        DummyRenderType,
        lambda value: f"<rendered:{value}>",
    )
    register.example = Style(DummyRenderType("example"))

    assert register.example == "<rendered:example>"

    register.mute()
    assert register.is_muted is True
    assert register.example == ""
    assert register("example") == ""

    register.unmute()

    assert register.is_muted is False
    assert isinstance(register.example, Style)
    assert register.example == "<rendered:example>"
    assert register("example") == "<rendered:example>"
    assert len(tuple(register.example.rules)) == 1
    assert isinstance(tuple(register.example.rules)[0], DummyRenderType)

# Generated at 2026-10-25 04:43:33.245829
# Unit test for method unmute of class Register
def test_Register_unmute():register = Register()

# Generated at 2026-10-25 04:43:35.663452
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:43:38.078868
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:43:48.368938
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:44:03.754339
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
    assert isinstance(register.example, Style)
    assert register.example == "<42>"
    assert tuple(register.example.rules) == (DummyRenderType(42),)

# Generated at 2026-10-25 04:44:29.587802
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:44:32.004747
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:44:34.418392
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:44:36.943405
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:44:39.358573
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:44:40.733917
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():
    from typing import Tuple

    class Dummy(RenderType):
        args: Tuple[int, ...]

    old_render = lambda *args: f"\x1b[{args[0]}m"
    new_render = lambda *args: f"<{args[0]}>"

    # --- Case 1: replaces the renderfunc in the registry ---
    reg = Register()
    reg.renderfuncs = {Dummy: old_render}
    reg.set_renderfunc(Dummy, new_render)
    assert reg.renderfuncs[Dummy] is new_render

    # --- Case 2: re-renders existing Style attributes with the new func ---
    reg2 = Register()
    reg2.renderfuncs = {Dummy: old_render}
    reg2.red = Style(Dummy(31))
    assert str(reg2.red) == "\x1b[31m"  # rendered with old func

    reg2.set_renderfunc(Dummy, new_render)
    assert str(reg2.red) == "<31>"      # re-rendered with new func

    # --- Case 3: rules are preserved after re-render (can re-render again) ---
    assert isinstance(reg2.red.rules[0], Dummy)
    reg2.set_renderfunc(Dummy, old_render)
    assert str(reg2.red) == "\x1b[31m"

# Generated at 2026-10-25 04:44:54.850861
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():register = Register()

# Generated at 2026-10-25 04:45:09.494918
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 04:45:24.720669
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():register = Register()

# Generated at 2026-10-25 04:45:26.071795
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

# Generated at 2026-10-25 04:45:27.420736
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

# Generated at 2026-10-25 04:45:28.760191
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

# Generated at 2026-10-25 04:45:31.390994
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 04:45:33.820249
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 04:45:36.250117
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 04:45:38.663511
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:45:47.788674
# Unit test for method unmute of class Register
def test_Register_unmute():register = Register()

# Generated at 2026-10-25 04:46:10.934604
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-25 04:46:17.179905
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():register = Register()

# Generated at 2026-10-25 04:46:18.511531
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

# Generated at 2026-10-25 04:46:19.877219
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

# Generated at 2026-10-25 04:46:21.230889
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

# Generated at 2026-10-25 04:46:22.608707
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

# Generated at 2026-10-25 04:46:24.559147
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

# Generated at 2026-10-25 04:46:25.888725
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

# Generated at 2026-10-25 04:47:11.656932
# Unit test for method unmute of class Register
def test_Register_unmute():
    class TestRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(TestRenderType, lambda value: f"<{value}>")
    register.example = Style(TestRenderType(42))

    assert register.example == "<42>"

    register.mute()
    assert register.is_muted is True
    assert register.example == ""

    register.unmute()
    assert register.is_muted is False
    assert register.example == "<42>"
    assert register.example.rules == (TestRenderType(42),)

# Generated at 2026-10-25 04:47:28.145923
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

# Generated at 2026-10-25 04:47:30.565030
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:47:32.980811
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:47:35.395162
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:47:37.811009
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:47:40.228659
# Unit test for method mute of class Register

# Generated at 2026-10-25 04:47:42.646004
# Unit test for method mute of class Register

# Generated at 2026-10-25 04:47:45.068497
# Unit test for method mute of class Register

# Generated at 2026-10-25 04:47:47.484341
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:47:49.899270
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:47:52.319267
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:47:54.732709
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:47:57.148252
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:47:59.563906
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:48:01.989285
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:48:04.405416
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:48:06.820234
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:48:09.235797
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:48:11.649500
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:48:14.064748
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:48:16.479494
# Unit test for method as_dict of class Register

# Generated at 2026-10-25 04:48:18.894011
# Unit test for method as_dict of class Register

# Generated at 2026-10-25 04:48:21.308692
# Unit test for method as_dict of class Register

# Generated at 2026-10-25 04:48:23.723401
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:48:26.139807
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:48:28.553362
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:48:30.967973
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:48:33.382419
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:48:35.797327
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:48:38.211519
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:48:40.626780
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:48:43.041377
# Unit test for method unmute of class Register

# Generated at 2026-10-25 04:48:45.456247
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:48:47.870499
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:48:50.284887
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-25 04:49:05.324373
# Unit test for method unmute of class Register
def test_Register_unmute():
    class TestRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(TestRenderType, lambda value: f"<{value}>")
    register.example = Style(TestRenderType("test"))

    assert register.example == "<test>"

    register.mute()
    assert register.is_muted is True
    assert register.example == ""

    register.unmute()
    assert register.is_muted is False
    assert register.example == "<test>"

# Generated at 2026-10-25 04:49:16.585942
# Unit test for method unmute of class Register
def test_Register_unmute():register = Register()

register.mute()
assert register.is_muted is True
assert register(42) == ""

register.unmute()
assert register.is_muted is False
assert register(42) == 42
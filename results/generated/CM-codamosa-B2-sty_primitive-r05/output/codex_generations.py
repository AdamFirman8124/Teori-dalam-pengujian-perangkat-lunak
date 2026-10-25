

# Generated at 2026-10-24 21:49:30.411318
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 21:49:32.826316
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 21:49:35.244440
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 21:49:37.662015
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:49:40.078622
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:49:42.495457
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:49:44.913489
# Unit test for method set_eightbit_call of class Register

# Generated at 2026-10-24 21:49:47.330073
# Unit test for method set_eightbit_call of class Register

# Generated at 2026-10-24 21:49:49.746041
# Unit test for method set_eightbit_call of class Register

# Generated at 2026-10-24 21:49:52.162059
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 21:49:54.580158
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 21:49:56.999702
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 21:50:09.080876
# Unit test for constructor of class Style
def test_Style():empty = Style()

# Generated at 2026-10-24 21:50:27.207010
# Unit test for method unmute of class Register
def test_Register_unmute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(
        DummyRenderType,
        lambda code: f"\x1b[{code}m",
    )

    rule = DummyRenderType(31)
    register.example = Style(rule)

    assert register.example == "\x1b[31m"

    register.mute()
    assert register.is_muted is True
    assert register.example == ""

    register.unmute()

    assert register.is_muted is False
    assert isinstance(register.example, Style)
    assert register.example == "\x1b[31m"
    assert tuple(register.example.rules) == (rule,)

# Generated at 2026-10-24 21:50:28.537412
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

# Generated at 2026-10-24 21:50:29.862528
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

# Generated at 2026-10-24 21:50:32.286158
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:50:35.404943
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:50:37.932863
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:50:40.352071
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:50:42.775238
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:50:45.194389
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:50:47.611670
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:50:50.028918
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:50:52.445291
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:50:54.861290
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:50:57.282892
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:50:59.700453
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:51:27.616045
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-24 21:51:55.475572
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-24 21:51:58.008273
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:52:00.429416
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:52:10.597528
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:52:11.960013
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

# Generated at 2026-10-24 21:52:25.771603
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    register = Register()

    # Plain strings are accepted by Register.__setattr__.
    register.red = "\x1b[31m"
    register.green = "\x1b[32m"
    register._private_style = "\x1b[34m"
    register.non_string = 42

    assert register.as_dict() == {
        "green": "\x1b[32m",
        "red": "\x1b[31m",
    }

# Generated at 2026-10-24 21:52:27.219054
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:52:34.286754
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():register = Register()

# Generated at 2026-10-24 21:52:36.809524
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:52:39.426017
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:52:41.875344
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:52:44.273944
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:52:46.692765
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:52:49.280522
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:52:51.695724
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:52:54.116927
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:52:56.535175
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:52:58.951959
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:53:01.370459
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:53:03.787727
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:53:06.209866
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:53:08.625235
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:53:11.040070
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:53:13.456934
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:53:15.874127
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:53:18.292300
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:53:20.712077
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:53:23.127432
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:53:25.545461
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:53:27.964049
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:53:30.381493
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:53:32.799600
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:53:35.216955
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:53:37.632596
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:53:40.049706
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:53:42.465059
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:53:44.882214
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:53:47.298339
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:53:49.716051
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:53:52.132475
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:53:54.549614
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:53:56.966632
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:53:59.382630
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:54:01.798424
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:54:04.218953
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:54:06.634431
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:54:09.053595
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:54:11.471046
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:54:13.890078
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:54:16.307144
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:54:18.725046
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:54:21.142141
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:54:23.558672
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:54:25.975263
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:54:28.394825
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:54:30.811499
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:54:33.228129
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:54:35.646745
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:54:38.064172
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:54:40.481721
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:54:42.896555
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:54:45.313944
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:54:47.732402
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:54:50.151644
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:54:52.568140
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:54:54.985060
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:55:07.991159
# Unit test for constructor of class Register
def test_Register():reg = Register()

# Generated at 2026-10-24 21:55:09.525307
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

# Generated at 2026-10-24 21:55:10.886216
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

# Generated at 2026-10-24 21:55:12.253546
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

# Generated at 2026-10-24 21:55:13.614961
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

# Generated at 2026-10-24 21:55:15.057272
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

# Generated at 2026-10-24 21:55:16.449531
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

# Generated at 2026-10-24 21:55:17.768148
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:55:27.242857
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():register = Register()

# Generated at 2026-10-24 21:55:30.012791
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:55:32.524602
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:55:35.052489
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:55:37.580286
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:55:40.151974
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:55:42.568641
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:55:45.090316
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:55:47.508760
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:55:49.926059
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:55:52.343821
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:55:54.760130
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:55:57.178538
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:55:59.598118
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:56:02.016755
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:56:14.743331
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-24 21:56:16.187595
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

# Generated at 2026-10-24 21:56:17.620018
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

# Generated at 2026-10-24 21:56:18.998366
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

# Generated at 2026-10-24 21:56:47.252080
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-24 21:56:49.671272
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:56:52.087180
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:56:54.503601
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:56:56.922587
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:56:59.338816
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:57:01.754562
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:57:04.168721
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:57:06.583303
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:57:08.999713
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:57:11.482202
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

# Generated at 2026-10-24 21:57:38.704059
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-24 21:57:40.108548
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:57:48.346333
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():register = Register()

# Generated at 2026-10-24 21:57:50.992194
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:57:53.503643
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:57:55.921323
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:57:58.349805
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:58:00.775445
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:58:03.196226
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:58:05.611265
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:58:08.174818
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:58:10.597021
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:58:13.015795
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:58:15.431482
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:58:17.847145
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:58:20.262967
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:58:22.679859
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 21:58:37.855365
# Unit test for method __call__ of class Register
def test_Register___call__():register = Register()

# Generated at 2026-10-24 21:58:51.514623
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

    assert register.example == "<42>"

    register.mute()
    assert register.is_muted is True
    assert register.example == ""
    assert register.example.rules == (DummyRenderType(42),)

    register.unmute()

    assert register.is_muted is False
    assert isinstance(register.example, Style)
    assert register.example == "<42>"
    assert register.example.rules == (DummyRenderType(42),)

# Generated at 2026-10-24 21:58:52.837773
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

# Generated at 2026-10-24 21:58:54.162280
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

# Generated at 2026-10-24 21:58:55.484249
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:59:09.654846
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:59:12.176320
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 21:59:20.433379
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:59:22.850240
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:59:25.265986
# Unit test for constructor of class Register

# Generated at 2026-10-24 21:59:27.683432
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:59:30.101651
# Unit test for method unmute of class Register

# Generated at 2026-10-24 21:59:31.514766
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


# Generated at 2026-10-24 19:48:02.884819
# Unit test for method as_namedtuple of class Register

# Generated at 2026-10-24 19:48:04.216940
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

# Generated at 2026-10-24 19:48:05.608033
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

# Generated at 2026-10-24 19:48:23.016009
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    register.renderfuncs[DummyRenderType] = lambda value: f"<{value}>"

    first_rule = DummyRenderType(1)
    second_rule = DummyRenderType(2)

    # Styles are rendered and nested styles are flattened.
    register.example = Style(first_rule, Style(second_rule))

    assert isinstance(register.example, Style)
    assert str(register.example) == "<1><2>"
    assert register.example.rules == (first_rule, second_rule)

    # Styles assigned while muted retain their rules but render as empty strings.
    register.is_muted = True
    muted_style = Style(first_rule)
    register.muted_example = muted_style

    assert isinstance(register.muted_example, Style)
    assert str(register.muted_example) == ""
    assert register.muted_example.rules == (first_rule,)

    # Non-Style values are assigned unchanged.
    sentinel = object()
    register.regular_attribute = sentinel

    assert register.regular_attribute is sentinel

# Generated at 2026-10-24 19:48:25.448430
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:48:27.879218
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:48:30.296816
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:48:32.714618
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:48:35.135989
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:48:37.551057
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:48:39.969664
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:48:42.391514
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:48:44.806630
# Unit test for constructor of class Style

# Generated at 2026-10-24 19:48:47.224562
# Unit test for constructor of class Style

# Generated at 2026-10-24 19:48:49.643372
# Unit test for constructor of class Style

# Generated at 2026-10-24 19:48:52.063705
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:48:54.481182
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:48:56.896490
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:48:59.312660
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:49:01.729157
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:49:04.149938
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:49:06.564827
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:49:09.015768
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:49:33.875631
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:49:51.795801
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:50:10.636878
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:50:13.170387
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:50:15.589168
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:50:18.120628
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:50:20.542231
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:50:22.957516
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 19:50:25.374677
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 19:50:27.796144
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 19:50:30.367444
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 19:50:32.794072
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 19:50:35.209993
# Unit test for method as_dict of class Register

# Generated at 2026-10-24 19:50:37.626231
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:50:40.041003
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:50:42.458253
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:50:44.875687
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:50:47.313036
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:50:49.716107
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:50:52.132357
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:50:54.549427
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:50:56.968745
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:50:59.390998
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:51:01.805122
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:51:06.651311
# Unit test for constructor of class Register
def test_Register():register = Register()

# Generated at 2026-10-24 19:51:19.246146
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:51:21.957658
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:51:24.636430
# Unit test for method __setattr__ of class Register

# Generated at 2026-10-24 19:51:35.630474
# Unit test for method mute of class Register
def test_Register_mute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(DummyRenderType, lambda value: f"<{value}>")
    register.example = Style(DummyRenderType(42))

    assert register.is_muted is False
    assert register.example == "<42>"

    register.mute()

    assert register.is_muted is True
    assert register.example == ""
    assert isinstance(register.example, Style)
    assert register.example.rules == (DummyRenderType(42),)
    assert register(42) == ""
    assert register("example") == ""

# Generated at 2026-10-24 19:51:38.048651
# Unit test for method mute of class Register

# Generated at 2026-10-24 19:51:40.468338
# Unit test for method mute of class Register

# Generated at 2026-10-24 19:51:42.884364
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:51:45.306492
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:51:47.723412
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:51:50.139622
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:51:52.555168
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:51:54.974334
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:51:57.549643
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:51:59.966563
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:52:02.384038
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:52:04.800678
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:52:07.216589
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:52:09.633850
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:52:12.047563
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 19:52:14.465362
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 19:52:16.881196
# Unit test for method __call__ of class Register

# Generated at 2026-10-24 19:52:19.299119
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:52:21.716691
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:52:24.133142
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:52:26.552576
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:52:28.967993
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:52:31.385334
# Unit test for constructor of class Register

# Generated at 2026-10-24 19:52:33.801051
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:52:36.217863
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:52:38.633635
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:52:41.050709
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:52:43.468257
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:52:45.887163
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:52:48.304167
# Unit test for method mute of class Register

# Generated at 2026-10-24 19:52:50.721700
# Unit test for method mute of class Register

# Generated at 2026-10-24 19:52:53.137331
# Unit test for method mute of class Register

# Generated at 2026-10-24 19:52:55.556225
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:52:57.973782
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:53:07.175365
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:53:08.505344
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:53:17.922569
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:53:26.734184
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():register = Register()

# Generated at 2026-10-24 19:53:49.670395
# Unit test for method unmute of class Register
def test_Register_unmute():
    register = Register()
    register.set_renderfunc(RenderType, lambda value: f"<{value}>")

    rule = RenderType(42)
    register.example = Style(rule)

    assert register.example == "<42>"

    register.mute()
    assert register.is_muted is True
    assert register.example == ""

    register.unmute()
    assert register.is_muted is False
    assert isinstance(register.example, Style)
    assert register.example == "<42>"
    assert tuple(register.example.rules) == (rule,)

# Generated at 2026-10-24 19:53:52.090651
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:53:54.606749
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:53:57.020101
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:53:59.580926
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:54:01.996834
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:54:04.414036
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:54:06.832268
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:54:09.249556
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:54:11.665923
# Unit test for method mute of class Register

# Generated at 2026-10-24 19:54:47.016852
# Unit test for method mute of class Register
def test_Register_mute():register = Register()

# Generated at 2026-10-24 19:54:48.349711
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:54:58.383238
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:55:00.801946
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:55:03.217455
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:55:05.635745
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:55:08.054074
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:55:10.470462
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:55:12.886961
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:55:15.304408
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:55:17.722464
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:55:20.138011
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:55:22.553947
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:55:24.969679
# Unit test for method mute of class Register

# Generated at 2026-10-24 19:55:27.387444
# Unit test for method mute of class Register

# Generated at 2026-10-24 19:55:29.802993
# Unit test for method mute of class Register

# Generated at 2026-10-24 19:55:32.218386
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:55:34.636303
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:55:37.054228
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:55:39.470650
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:55:41.888737
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:55:44.305454
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:55:56.753538
# Unit test for method set_renderfunc of class Register
def test_Register_set_renderfunc():register = Register()


# Generated at 2026-10-24 19:56:12.088631
# Unit test for method unmute of class Register
def test_Register_unmute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    rule = DummyRenderType("example")

    register.set_renderfunc(DummyRenderType, lambda value: f"<{value}>")
    register.example = Style(rule)

    assert str(register.example) == "<example>"

    register.mute()
    assert register.is_muted is True
    assert str(register.example) == ""

    register.unmute()

    assert register.is_muted is False
    assert str(register.example) == "<example>"
    assert tuple(register.example.rules) == (rule,)

# Generated at 2026-10-24 19:56:13.428062
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

# Generated at 2026-10-24 19:56:14.753885
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

# Generated at 2026-10-24 19:56:16.093284
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:56:25.764363
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:56:33.630602
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:56:36.153675
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:56:38.571313
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:56:40.990282
# Unit test for method set_renderfunc of class Register

# Generated at 2026-10-24 19:56:44.297339
# Unit test for method mute of class Register

# Generated at 2026-10-24 19:56:46.718210
# Unit test for method mute of class Register

# Generated at 2026-10-24 19:56:49.132419
# Unit test for method mute of class Register

# Generated at 2026-10-24 19:56:51.548884
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:56:53.979622
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:56:56.397646
# Unit test for method unmute of class Register

# Generated at 2026-10-24 19:57:14.178247
# Unit test for method unmute of class Register
def test_Register_unmute():from sty import Register, Style

# Generated at 2026-10-24 19:57:32.603658
# Unit test for method mute of class Register
def test_Register_mute():
    class DummyRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(DummyRenderType, lambda value: f"<{value}>")

    rule = DummyRenderType(42)
    register.example = Style(rule)

    assert register.is_muted is False
    assert register.example == "<42>"

    register.mute()

    assert register.is_muted is True
    assert isinstance(register.example, Style)
    assert register.example == ""
    assert tuple(register.example.rules) == (rule,)

    # All direct register calls should also be muted.
    assert register(42) == ""
    assert register("example") == ""
    assert register(1, 2, 3) == ""

# Generated at 2026-10-24 19:57:39.870006
# Unit test for method mute of class Register
def test_Register_mute():register = Register()

# Generated at 2026-10-24 19:57:56.560608
# Unit test for method mute of class Register
def test_Register_mute():
    class TestRenderType(RenderType):
        pass

    register = Register()
    register.set_renderfunc(
        TestRenderType,
        lambda value: f"<{value}>",
    )

    rule = TestRenderType(42)
    register.example = Style(rule)

    assert register.is_muted is False
    assert register.example == "<42>"

    register.mute()

    assert register.is_muted is True
    assert isinstance(register.example, Style)
    assert register.example == ""
    assert tuple(register.example.rules) == (rule,)

    # All call variants should return an empty string while muted.
    assert register(42) == ""
    assert register(1, 2, 3) == ""
    assert register("example") == ""
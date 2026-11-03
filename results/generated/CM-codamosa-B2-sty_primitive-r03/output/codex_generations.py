

# Generated at 2026-11-01 19:55:41.044772
# Unit test for method __call__ of class Register

# Generated at 2026-11-01 19:56:56.966342
# Unit test for method __call__ of class Register
def test_Register___call__():
    reg = Register()

    # Single int argument -> dispatched to eightbit_call (identity by default)
    assert reg(42) == 42

    # Three int arguments -> dispatched to rgb_call (returns tuple by default)
    assert reg(10, 20, 30) == (10, 20, 30)

    # Single string argument -> attribute lookup on the register
    reg.orange = "ORANGE_VALUE"
    assert reg("orange") == "ORANGE_VALUE"

    # Zero or two arguments -> unsupported, returns empty string
    assert reg() == ""
    assert reg(1, 2) == ""

    # Muted register returns empty string for all call forms
    reg.mute()
    assert reg(42) == ""
    assert reg(10, 20, 30) == ""
    assert reg("orange") == ""

    # After unmuting, calls work again
    reg.unmute()
    assert reg(42) == 42
    assert reg(10, 20, 30) == (10, 20, 30)
    assert reg("orange") == "ORANGE_VALUE"

# Generated at 2026-11-01 19:58:50.940377
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    # Create a Register instance
    register = Register()

    # Define a fake rendertype and a mock render function
    class FakeRendertype(RenderType):
        pass

    def fake_rgb_render(r, g, b):
        return f"rgb({r},{g},{b})"

    # Set up the renderfuncs dict with the fake rendertype
    register.renderfuncs[FakeRendertype] = fake_rgb_render

    # Call set_rgb_call with the fake rendertype
    register.set_rgb_call(FakeRendertype)

    # Assert that rgb_call has been updated to the fake render function
    assert register.rgb_call is fake_rgb_render

    # Test that calling the register with 3 args uses the new rgb_call
    result = register(1, 2, 3)
    assert result == "rgb(1,2,3)"

    # Test that the original rgb_call was different before set_rgb_call was invoked
    register2 = Register()
    assert register2.rgb_call is not fake_rgb_render
    assert register2.rgb_call(1, 2, 3) == (1, 2, 3)

# Generated at 2026-11-01 19:59:31.284514
# Unit test for method set_eightbit_call of class Register
def test_Register_set_eightbit_call():
    reg = Register()

    # Sanity check: by default the eightbit_call is an identity function.
    assert reg.eightbit_call(42) == 42

    # Prepare two fake rendertypes with their render functions.
    eightbit_rendertype = Mock(name="EightbitRendertype")
    rgb_rendertype = Mock(name="RgbRendertype")

    eightbit_renderfunc = Mock(
        name="eightbit_renderfunc", return_value="\x1b[38;5;42m"
    )
    rgb_renderfunc = Mock(
        name="rgb_renderfunc", return_value="\x1b[38;2;1;2;3m"
    )

    reg.renderfuncs = {
        eightbit_rendertype: eightbit_renderfunc,
        rgb_rendertype: rgb_renderfunc,
    }

    # Set the eightbit call to the eightbit renderfunc.
    reg.set_eightbit_call(eightbit_rendertype)

    # The eightbit_call attribute must now point to the registered renderfunc.
    assert reg.eightbit_call is eightbit_renderfunc
    assert reg.eightbit_call(42) == "\x1b[38;5;42m"
    eightbit_renderfunc.assert_called_once_with(42)

    # Calling set_eightbit_call again with another rendertype replaces the call.
    reg.set_eightbit_call(rgb_rendertype)
    assert reg.eightbit_call is rgb_renderfunc
    assert reg.eightbit_call(10, 20, 30) == "\x1b[38;2;1;2;3m"

    # The renderfunc itself must remain untouched in the registry.
    assert reg.renderfuncs[eightbit_rendertype] is eightbit_renderfunc
    assert reg.renderfuncs[rgb_rendertype] is rgb_renderfunc

# Generated at 2026-11-01 20:02:47.342803
# Unit test for method mute of class Register
def test_Register_mute():
    from sty.rendertype import RenderType

    class DummyRenderType(RenderType):
        pass

    reg = Register()

    # Register a render function for the dummy render type
    reg.renderfuncs[DummyRenderType] = lambda x: "\x1b[{}m".format(x)

    # Create a style attribute; it is rendered immediately upon assignment
    reg.orange = Style(DummyRenderType(42), value="\x1b[42m")

    # Sanity checks before muting
    assert reg.is_muted is False
    assert str(reg.orange) == "\x1b[42m"

    # Mute the register
    reg.mute()

    # The register is muted now
    assert reg.is_muted is True

    # All style attributes are re-rendered to empty strings
    assert str(reg.orange) == ""
    assert isinstance(reg.orange, Style)

    # Calls on a muted register return empty strings
    assert reg("orange") == ""
    assert reg(42) == ""
    assert reg(1, 2, 3) == ""

    # Unmuting restores the rendered styles
    reg.unmute()
    assert reg.is_muted is False
    assert str(reg.orange) == "\x1b[42m"

    # Muting again keeps behavior consistent (idempotent)
    reg.mute()
    assert reg.is_muted is True
    assert str(reg.orange) == ""

# Generated at 2026-11-01 20:04:24.232404
# Unit test for method set_renderfunc of class Register
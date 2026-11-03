

# Generated at 2026-11-02 11:19:47.801269
# Unit test for method set_rgb_call of class Register
def test_Register_set_rgb_call():
    """
    set_rgb_call should replace the register's rgb_call with the render
    function that is registered for the given rendertype.
    """
    register = Register()

    # The default rgb_call is a passthrough
    assert register.rgb_call(1, 2, 3) == (1, 2, 3)

    # Create a fake rendertype and a fake render function
    rendertype = mock.Mock()
    render_func = mock.Mock(return_value="rendered")

    # Register the render function for the rendertype
    register.set_renderfunc(rendertype, render_func)

    # rgb_call should still be untouched after set_renderfunc
    assert register.rgb_call(1, 2, 3) == (1, 2, 3)

    # Set the rgb call to use the new rendertype's render function
    register.set_rgb_call(rendertype)

    assert register.rgb_call is render_func
    assert register.rgb_call(10, 20, 30) == "rendered"
    assert render_func.call_args == mock.call(10, 20, 30)

    # Calling the register with 3 args should use the new rgb_call
    assert register(10, 20, 30) == "rendered"

# Generated at 2026-11-02 11:24:33.325539
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    register = Register()

    # A register without any style attributes exports an empty dict.
    assert register.as_dict() == {}

    def render_func(*args: int) -> str:
        return "\x1b[{}m".format(args[0])

    register.renderfuncs = {RenderType: render_func}

    # Assigning a Style triggers rendering via the register's renderfuncs.
    register.red = Style(RenderType(31))
    register.bold = Style(RenderType(1))

    # Private and non-string attributes must not be exported.
    register._private = "hidden"
    register.not_a_style = 42

    result = register.as_dict()

    assert isinstance(result, dict)
    assert set(result.keys()) == {"red", "bold"}
    assert result["red"] == "\x1b[31m"
    assert result["bold"] == "\x1b[1m"

# Generated at 2026-11-02 11:26:41.954292
# Unit test for method as_dict of class Register
def test_Register_as_dict():
    # An empty register should export an empty dict (non-str attributes are skipped).
    reg = Register()
    assert reg.as_dict() == {}

    # Add some styles to the register.
    reg.orange = Style(value="\x1b[38;2;1;5;10m")
    reg.blue = Style(value="\x1b[38;2;0;0;255m")

    result = reg.as_dict()

    # Only string-like attributes (Style is a str subclass) should be exported,
    # and their values should be their rendered string representations.
    assert result == {
        "orange": "\x1b[38;2;1;5;10m",
        "blue": "\x1b[38;2;0;0;255m",
    }
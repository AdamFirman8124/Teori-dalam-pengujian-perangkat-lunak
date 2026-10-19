

# Generated at 2022-06-14 08:08:02.822650
# Unit test for function mute
def test_mute():
    from .sequential import Register
    from .hdl import Always_Comb, assign
    from .simulation import run_simulation
    from .meta import get_ports

    clk = port.Clock("clk")

    @Register
    class reg:
        def __init__(self):
            self.din = port.Input(4, "din")
            self.dout = port.Output(4, "dout")

            self.clk = port.Internal(8, "clk")
            self.dout <<= self.din

    @Always_Comb
    def beh_reg():
        reg.clk <<= clk

    reg2 = reg()
    print(reg2)
    print("Ports before mutation:", get_ports(reg2))

    reg2.mute()

# Generated at 2022-06-14 08:08:06.994020
# Unit test for function mute
def test_mute():
    r1 = Register(name="r1", clocking=True)
    r2 = Register(name="r2", clocking=True)
    mute(r1, r2)
    assert r1.muted
    assert r2.muted



# Generated at 2022-06-14 08:08:10.106213
# Unit test for function mute
def test_mute():
    toggle = Register("", 8, 0x00)
    mute(toggle)
    assert toggle.muted() == True


# Generated at 2022-06-14 08:08:15.806471
# Unit test for function mute
def test_mute():
    a = Register(2, name="a")
    b = Register(2, name="b")
    c = Register(2, name="c")
    mute(a, b, c)
    assert a.is_muted is True
    assert b.is_muted is True
    assert c.is_muted is True


# Generated at 2022-06-14 08:08:17.238603
# Unit test for function unmute
def test_unmute():
    assert unmute() is None

# Generated at 2022-06-14 08:08:20.324960
# Unit test for function unmute
def test_unmute():
    reg = Register(name='reg', width=4)
    reg.unmute()
    assert(not reg.mute_val)

# Generated at 2022-06-14 08:08:25.834843
# Unit test for function unmute
def test_unmute():
    """
    A >>> unmute(x, y, z)
         ...
    B >>> x.is_muted == False
    C >>> y.is_muted == False
    D >>> z.is_muted == False
    """
    pass



# Generated at 2022-06-14 08:08:30.426733
# Unit test for function mute
def test_mute():
    """Unit test for function mute"""
    r = Register()
    assert r.is_muted() is False
    mute(r)
    assert r.is_muted() is True


# Generated at 2022-06-14 08:08:37.113889
# Unit test for function unmute
def test_unmute():
    """
    Test function unmute.
    """
    # Initialise register-objects
    gari = Register(0, "gari")
    jari = Register(1, "jari")

    # Mute the registers
    mute(gari, jari)

    # Test if the registers are muted
    assert gari.is_muted() == True
    assert jari.is_muted() == True

    # Unmute the registers
    unmute(gari, jari)

    # Test if the registers are unmuted
    assert gari.is_muted() == False
    assert jari.is_muted() == False



# Generated at 2022-06-14 08:08:49.675118
# Unit test for function mute
def test_mute():
    """
    Test the mute() function.
    """
    a = Register(0, 1)
    b = Register(0, 1)
    c = Register(0, 1)

    # Check if the mute()-method works with the register-class
    mute(a, b)
    assert a == 0
    assert b == 0
    assert c == 0

    # Check if the mute()-method works with multiple registers
    a.value = 1
    mute(a, b, c)
    assert a == 0
    assert b == 0
    assert c == 0

    # Check if it can handle a single register
    c.value = 1
    mute(c)
    assert c == 0

    # Check if the function can handle wrong input
    def test_input() -> None:
        mute("foo", 3, False)
    assert_
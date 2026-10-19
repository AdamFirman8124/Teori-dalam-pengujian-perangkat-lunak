

# Generated at 2022-06-14 08:07:55.900573
# Unit test for function mute
def test_mute():
    """
    Test the mute()-function by passing in a register and check if the
    register has been muted.
    """
    port = RPi.GPIO
    reg = Register(0x0, port)
    mute(reg)
    assert reg.is_muted


# Generated at 2022-06-14 08:08:05.799006
# Unit test for function unmute
def test_unmute():
    from .primitive import BitArray
    from .primitive import BitArrayRegister
    from .primitive import ByteArray
    from .primitive import ByteArrayRegister
    from .primitive import WordArray
    from .primitive import WordArrayRegister

    BitArrayRegister(name='barr1', width=3, value=1)
    BitArrayRegister(name='barr2', width=6, value=0b111111)
    ByteArrayRegister(name='bytearr1', width=8, value=0b10101010)
    ByteArrayRegister(name='bytearr2', width=12, value=0b1100011_01011010)
    WordArrayRegister(name='wordarr1', width=4, value=0b0011_1100_0011_1100)

# Generated at 2022-06-14 08:08:16.741654
# Unit test for function mute
def test_mute():
    from .settings import set_debug
    set_debug(False)

    from .primitive import Bit
    from .register import Register
    from . import settings
    from .bus import Bus
    self_bus = Bus("self_bus")
    settings.bus = self_bus

    bit1 = Bit("bit1")
    bit2 = Bit("bit2")
    reg1 = Register("reg1", bits=[bit1, bit2])
    reg1.set(3)
    mute(reg1)
    assert reg1.get() != 3
    unmute(reg1)

    assert reg1.get() == 3
    settings.bus.shutdown()



# Generated at 2022-06-14 08:08:19.235262
# Unit test for function mute
def test_mute():
    reg = Register(label=0)
    assert not reg.muted
    mute(reg)
    assert reg.muted

# Generated at 2022-06-14 08:08:23.702222
# Unit test for function mute
def test_mute():
    from .primitive import I2CRegister

    i2c = I2CRegister(0x5a, 1, 0x00)
    mute(i2c)

    assert i2c._mute == True



# Generated at 2022-06-14 08:08:35.344041
# Unit test for function mute
def test_mute():
    # Test unmute on register-objects created by the primitive class
    r1 = Register()
    r2 = Register()
    r3 = Register()
    r1.mute()
    mute(r2, r3)
    assert r1.get_state() == r2.get_state() == r3.get_state() == 'muted'
    unmute(r2, r3)
    assert r1.get_state() == 'muted'
    assert r2.get_state() == r3.get_state() == 'unmuted'
    r1.unmute()
    assert r1.get_state() == 'unmuted'
    try:
        mute('a', 3)
    except ValueError as e:
        assert type(e) == ValueError



# Generated at 2022-06-14 08:08:44.490775
# Unit test for function mute
def test_mute():
    from .primitive import Switch

    _s = Switch(8)
    _s.mute()
    assert all(_s.read() == 0 for _ in range(8))
    _s.unmute()
    # Check 11
    _s.set_value(0b00001011)
    _s.mute()
    assert _s.read() == 0
    _s.unmute()
    assert _s.read() == 0b00001011
    _s.mute()
    _s.read()
    _s.read()
    _s.read()
    _s.read()
    _s.read()
    _s.set_value(0)
    _s.unmute()
    assert _s.read() == 0
    _s.reset()
    _s.mute

# Generated at 2022-06-14 08:08:48.699157
# Unit test for function unmute
def test_unmute():
    r = [Register()]*10
    assert r[3].state == False
    unmute(r[3])
    assert r[3].state == True
    return True

# Generated at 2022-06-14 08:08:55.937846
# Unit test for function mute
def test_mute():
    from .primitive import Register
    from .primitive import Bus


    reg1 = Register("reg1", width=4)
    reg2 = Register("reg2", width=4)

    bus1 = Bus("bus1", width=8)

    mute(reg1, reg2, bus1)
    assert reg1.muted == True
    assert reg2.muted == True
    assert bus1.muted == True



# Generated at 2022-06-14 08:09:07.246090
# Unit test for function mute
def test_mute():
    from ..core.logic import DFlipFlop
    from ..core.memory import RegisterFile

    d_flip_flop = DFlipFlop(d=1)

    d_flip_flop.sync()

    assert d_flip_flop.q == 0

    d_flip_flop.d = 0
    d_flip_flop.mute()
    d_flip_flop.sync()

    assert d_flip_flop.q == 0

    d_flip_flop.unmute()
    d_flip_flop.sync()

    assert d_flip_flop.q == 0

    register_file_0 = RegisterFile(4, [1, 0, 1, 1])
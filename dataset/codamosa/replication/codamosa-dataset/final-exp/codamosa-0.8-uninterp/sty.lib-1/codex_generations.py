

# Generated at 2022-06-14 08:07:55.678107
# Unit test for function mute
def test_mute():
    from . import Sequential
    Checkpoint = Sequential(mute, unmute, mute)
    assert Checkpoint[0].is_muted()
    assert not Checkpoint[1].is_muted()
    assert Checkpoint[2].is_muted()

# Generated at 2022-06-14 08:08:08.059975
# Unit test for function mute
def test_mute():
    """Unit tests for the function mute"""

    class MyRegister(Register):
        def __init__(self, *args, **kwargs):
            Register.__init__(self, *args, **kwargs)
            self.pulse_counter = 0

        def pulse(self, *args, **kwargs):
            # print("pulse...")
            self.pulse_counter += 1

    # Unit test: check that the function mute() works
    # Create a register and initialize it
    r1 = MyRegister(
        nbits=16,
        initval=-1,
        name='r1',
        pulse_mode='classic',
        var_idx_bits=0,
        var_name='r1'
    )

    # Create a register and initialize it

# Generated at 2022-06-14 08:08:14.229419
# Unit test for function unmute
def test_unmute():

    # Create object
    obj = Register(0x00, 0x00, bits=0)
    assert obj.get_value() == 0x00

    # Mute object
    obj.mute()
    assert obj.is_muted()

    # Mute object
    unmute(obj)
    assert obj.is_muted()

# Generated at 2022-06-14 08:08:27.289116
# Unit test for function unmute
def test_unmute():
    from .primitive import Bit, Byte
    from .primitive import Integer, String
    from .primitive import BitField, UIntField, SIntField
    from .primitive import Enum, Bool
    from .primitive import ByteArray
    from .primitive import Array, MultiArray
    from .primitive import Separator, VariableSeparator
    reg_empty = Register('Register empty') 
    reg_1 = Register('Register 1')
    reg_1.bit_a = BitField(7, name='bit_a')
    reg_1.bit_b = Bit(1, name='bit_b')
    reg_1.bit_c = Bit(1, name='bit_c')
    reg_2 = Register('Register 2')
    reg_2.bit_a = Bit(1, name='bit_a')


# Generated at 2022-06-14 08:08:36.364646
# Unit test for function mute
def test_mute():
    from pytest import approx

    # Define register object
    class Reg():
        def mute(self):
            print("muted!")
            self.value = 0
        def unmute(self):
            pass

    a = Reg()
    a.value = 1
    b = Reg()
    b.value = 5

    # Call function mute
    mute(a,b)

    # Check if mute function did what it was supposed to
    assert a.value == approx(0)
    assert b.value == approx(0)


# Generated at 2022-06-14 08:08:49.410254
# Unit test for function mute
def test_mute():
    from .register import Register
    from .register_function import RegisterFunction
    from .special import DigitCounter
    from .line_detector import LineDetector
    import pytest

    # Create the registers to be used
    a = Register(16)
    b = Register(16)
    c = Register(16)
    d = Register(16)
    e = Register(16)

    # Create the special register to be used
    f = DigitCounter(16)

    # Create the registers functions to be used
    f1 = RegisterFunction(f, a, b)
    f2 = RegisterFunction(f, c, d)

    # Create the line detector to be used
    g = LineDetector(16, 2)

    # Create the line detector function to be used
    f3 = RegisterFunction(g, a, b)

    #

# Generated at 2022-06-14 08:08:59.558293
# Unit test for function unmute
def test_unmute():
    from .fourbit import FourBitRegister
    r1 = FourBitRegister(0b1111)
    r2 = FourBitRegister(0b0000)
    r3 = FourBitRegister(0b1111)
    r4 = FourBitRegister(0b0000)

    mute(r1, r2, r3, r4)
    
    assert r1.get_value() == 0
    assert r2.get_value() == 0
    assert r3.get_value() == 0
    assert r4.get_value() == 0
    
    unmute(r1, r2, r3, r4)
    
    assert r1.get_value() == 0b1111
    assert r2.get_value() == 0b0000
    assert r3.get_value() == 0b1111
    assert r4.get_value

# Generated at 2022-06-14 08:09:09.172751
# Unit test for function mute
def test_mute():
    from . import xlib
    from .bit import Bit
    from .nibble import Nibble
    from .byte import Byte

    # Basic mute
    a = Bit(0, "a")
    b = Bit(1, "b")
    c = Bit(2, "c")
    d = Bit(3, "d")
    e = Bit(4, "e")
    f = Bit(5, "f")
    g = Bit(6, "g")
    h = Bit(7, "h")

    a.write(1)
    b.write(0)
    c.write(1)
    d.write(0)
    e.write(1)
    f.write(0)
    g.write(1)
    h.write(0)


# Generated at 2022-06-14 08:09:13.648455
# Unit test for function mute
def test_mute():
    from .primitive import dff
    assert dff().muted == False
    mute(dff())
    assert dff().muted == True


# Generated at 2022-06-14 08:09:18.853480
# Unit test for function mute
def test_mute():
    reg1 = Register("Test")
    reg2 = Register("Test2")
    reg1.value = 0b0101
    reg2.value = 0b1111

    mute(reg1, reg2)
    assert reg1.value == 0b0000
    assert reg2.value == 0b0000


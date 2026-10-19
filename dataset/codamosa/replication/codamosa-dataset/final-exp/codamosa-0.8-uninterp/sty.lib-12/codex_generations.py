

# Generated at 2022-06-14 08:07:57.735182
# Unit test for function mute
def test_mute():
    from .core import (
        Address,
        Unsigned,
        List,
        BitField,
        Subregister,
        Field,
        Register,
        DefaultRegister,
    )

    class Addr(Address):
        addr: Unsigned

    class AddrList(List, length=32):
        addr: Addr

    class Subreg(Subregister, position=0, width=7):
        subreg: Unsigned

    class BitField(BitField, bit=5):
        bf: Unsigned

    class Field(Field):
        value: Subreg
        bf: BitField

    class Reg(Register):
        addr: Addr
        field: Field

    reg = Reg()
    mute(reg)

    assert reg._is_mute



# Generated at 2022-06-14 08:08:09.535457
# Unit test for function mute
def test_mute():
    from .primitive import Byte
    from .primitive import BitField
    from .primitive import IntField
    from .primitive import EnumField
    from .primitive import StructField
    from .primitive import UnionField
    from .primitive import ArrayField
    from .primitive import ListField

    byte_a = Byte(0x00)
    byte_b = Byte(0x00)
    byte_c = Byte(0x00)
    byte_d = Byte(0x00)

    bit_a = BitField(byte_a, 0, 1, default=0b0, name='bit_a')
    bit_b = BitField(byte_a, 1, 1, default=0b1, name='bit_b')

# Generated at 2022-06-14 08:08:20.432939
# Unit test for function mute
def test_mute():
    from .primitive import Primitive
    prim = Primitive('test_mute', 0x0000)
    prim.create_registers(
        ('mute_test_reg', 'mute_test_field', 0x00ffff, 0, 'rw')
    )
    assert prim.mute_test_reg.field.read() == 0
    mute(prim.mute_test_reg)
    prim.mute_test_reg.field.write(0x00ff)
    assert prim.mute_test_reg.field.read() == 0
    unmute(prim.mute_test_reg)
    prim.mute_test_reg.field.write(0x00ff)
    assert prim.mute_test_reg.field.read() == 0xff



# Generated at 2022-06-14 08:08:22.886853
# Unit test for function unmute
def test_unmute():
    assert mute(0x0, 0x1) == None
    assert unmute(0x0, 0x1) == None

# Generated at 2022-06-14 08:08:29.813393
# Unit test for function mute
def test_mute():
    from .primitive import MMIO_REG_UNSIGNED_CHAR
    io = MMIO_REG_UNSIGNED_CHAR(0x32000000)
    io.name = "io"
    io.bitwidth = 8
    io.offset = 0
    io.reset = 0xAA

    mute(io)
    assert io.muted
    unmute(io)
    assert not io.muted

# Generated at 2022-06-14 08:08:41.589120
# Unit test for function mute
def test_mute():
    """
    Run a unit test on the function mute to check if the function works
    as intended.
    """
    obj = Register(0, 2, range(2), 3, 2)
    assert obj.muted is False, "Test failed. The initial value of 'muted' should be False."

    mute(obj)
    assert obj.muted is True, "Test failed. The 'muted' attribute should be True after executing mute()."

    mute(obj)
    assert obj.muted is True, "Test failed. The 'muted' attribute should remain True after executing mute() on an already muted object."

    unmute(obj)
    assert obj.muted is False, "Test failed. The 'muted' attribute should be False after executing unmute()."

    unmute(obj)

# Generated at 2022-06-14 08:08:42.665737
# Unit test for function mute
def test_mute():
    pass


# Generated at 2022-06-14 08:08:49.012675
# Unit test for function mute
def test_mute():
    register = Register(2, "R1")
    assert register.is_muted() == False
    mute(register)
    assert register.is_muted() == True
    unmute(register)
    assert register.is_muted() == False
    print("Unit test for function mute() did pass.")

test_mute()

# Generated at 2022-06-14 08:08:59.385248
# Unit test for function mute
def test_mute():
    r1 = Register(
        name="First Register",
        width=8,
        memory=False,
        name_override=True
    )
    r2 = Register(
        name="Second Register",
        width=16,
        memory=True,
        name_override=False
    )
    r3 = Register(
        name="Third Register",
        width=32,
        memory=True,
        name_override=True
    )
    r4 = Register(
        name="Fourth Register",
        width=64,
        memory=False,
        name_override=False
    )
    r5 = Register(
        name="Fifth Register",
        width=128,
        memory=True,
        name_override=True
    )

# Generated at 2022-06-14 08:09:08.544457
# Unit test for function unmute
def test_unmute():
    import pytest
    class TestRegister(Register):
        def __init__(self, i):
            super().__init__()
            self.i = i
    testRegisters = [TestRegister(i) for i in range(3)]
    mute(*testRegisters)
    for i, reg in enumerate(testRegisters):
        assert reg.mute_status == True
        assert reg.i == i
    unmute(*testRegisters)
    for i, reg in enumerate(testRegisters):
        assert reg.mute_status == False
        assert reg.i == i




# Generated at 2022-06-14 08:08:03.815822
# Unit test for function unmute
def test_unmute():
    from .primitive import ureg
    from .configuration import setup
    from . import example

    setup()
    mute(ureg)

    # Example register
    unmute(
        example.mcr_example, example.mcr_example.logger.log, example.mcr_example.logger.report
    )
    assert example.mcr_example.logger.log.mute == False
    assert example.mcr_example.logger.report.mute == False

    unmute(
        example.mcr_example, example.mcr_example.logger.log, example.mcr_example.logger.report
    )
    assert example.mcr_example.logger.log.mute == False
    assert example.mcr_example.logger.report.mute == False


# Generated at 2022-06-14 08:08:10.673808
# Unit test for function mute
def test_mute():
    from .primitive import Register
    err = ValueError(
        "The mute() method can only be used with objects that inherit "
        "from the 'Register class'."
    )
    reg1 = Register(nx=8)
    try:
        mute(reg1, reg1)
    except Exception as e:
        assert(isinstance(e, err))


# Generated at 2022-06-14 08:08:20.506811
# Unit test for function unmute
def test_unmute():
    from .primitive import LazyRegister
    from .primitive import Register
    reg = Register()
    reg.set_mute(True)
    assert reg.get_mute()

    # Test for unmuting a single Register
    unmute(reg)
    assert not reg.get_mute()

    # Test for unmuting a group of Registers
    reg1 = Register()
    reg2 = Register()
    reg3 = LazyRegister()
    regs = [reg1, reg2, reg3]
    mute(*regs)
    assert all([reg.get_mute() for reg in regs])

    unmute(*regs)
    assert all([not reg.get_mute() for reg in regs])



# Generated at 2022-06-14 08:08:22.027687
# Unit test for function mute
def test_mute():
    pass



# Generated at 2022-06-14 08:08:26.160913
# Unit test for function unmute
def test_unmute():
    from .primitive.register import MUX
    register = MUX(True)
    register.set_value(1)
    unmute(register)
    assert register.get_value() == 1



# Generated at 2022-06-14 08:08:37.370910
# Unit test for function mute
def test_mute():
    from .primitive import V
    # First define some objects
    tmp = V(0, "tmp")
    tmp1 = V(0, "tmp1")
    tmp2 = V(0, "tmp2")
    # Make some list of this objects
    objs = [tmp, tmp1, tmp2]
    # Mute all the objects
    mute(*objs)
    # Check if the objects are muted.
    assert all([obj.muted == True for obj in objs])
    # Unmute all the objects
    unmute(*objs)
    # Check if the objects are unmuted.
    assert all([obj.muted == False for obj in objs])

# Generated at 2022-06-14 08:08:45.520205
# Unit test for function mute
def test_mute():
    """
    Use a dummy class that inherits from the 'Register' class to test if
    the mute() function works as expected.
    """
    class DummyRegister(Register):
        def __init__(self, label: str, address: int, bitsize: int):
            super().__init__(
                label=label, address=address, bitsize=bitsize,
                readonly=False, signed=False, minval=0, maxval=0,
                clear_bit=False
            )
            self.value = 0
            self.muted = False

        def _get_bits(self) -> BitSequence:
            raise NotImplementedError()

        def _set_bits(self, value: BitSequence) -> None:
            raise NotImplementedError()


# Generated at 2022-06-14 08:08:52.177108
# Unit test for function mute
def test_mute():
    r1 = Register(3)
    r2 = Register(3)
    r1.set_value(0b110)
    r2.set_value(0b101)
    mute(r1, r2)
    assert r1.is_muted() is True
    assert r2.is_muted() is True


# Generated at 2022-06-14 08:08:58.699093
# Unit test for function unmute
def test_unmute():
    from .primitive import Register
    r = Register(32)
    assert r.masked == 0
    r.mute()
    assert r.masked == 0
    r.value = 15
    assert r.masked == 0
    r.unmute()
    assert r.masked == 15


# Generated at 2022-06-14 08:09:10.878428
# Unit test for function unmute
def test_unmute():
    # Checking if unmute() function works correctly.
    from .register import Reg
    from .primitive import DataType
    from warnings import warn
    with warn(ResourceWarning):
        # Create two Reg objects.
        reg1 = Reg(name="reg1", address=0x0, default_value=0x0, data_type=DataType.UINT32)
        reg2 = Reg(name="reg2", address=0x0, default_value=0x0, data_type=DataType.UINT32)
        # Mute two Reg objects.
        mute(reg1, reg2)
        # Check if the two Reg objects are muted.
        assert reg1.is_muted
        assert reg2.is_muted

        # Unmute two Reg objects.
        unmute(reg1, reg2)
        # Check


# Generated at 2022-06-14 08:07:50.530905
# Unit test for function mute
def test_mute():
    if not isinstance(mute(), None):
        raise AssertionError("Function mute() does not return None.")


# Generated at 2022-06-14 08:08:03.168869
# Unit test for function unmute
def test_unmute():
    import numpy as np

    # Check that unmute raises an error if any of the objects are not in fact
    # regiters
    with pytest.raises(ValueError):
        class Dummy:
            pass
        unmute(Dummy())

    # Check that unmute raises an error if any of the objects are not in fact
    # registers
    with pytest.raises(ValueError):
        class Dummy:
            pass
        unmute(Dummy(), Dummy())

    # Check that the function works as expected
    a = Register(np.arange(10))
    b = Register(np.random.randn(10))
    mute(a, b)
    assert a.mute_count == 1
    assert b.mute_count == 1
    unmute(a, b)
    assert a.mute

# Generated at 2022-06-14 08:08:11.546732
# Unit test for function unmute
def test_unmute():
    import dvbcss.monotonic_time as time
    from dvbcss.clock import SysClock
    from dvbcss.protocol.ts import PcrPid
    from dvbcss.protocol.ts import Pid

    class TestRegister(Register):
        def __init__(self, pid, smoothingEnabled=False):
            super().__init__(pid, smoothingEnabled)
            self.queue = []

        def _readPacket(self):
            return self.queue.pop(0)

        def queuePacket(self, pkt):
            self.queue.append(pkt)

# Generated at 2022-06-14 08:08:17.421924
# Unit test for function unmute
def test_unmute():
    class Reg(Register):
        def __init__(self, name="test"):
            super().__init__(name)

    r = Reg()
    assert r.unmuted
    r.mute()
    assert r.muted
    r.unmute()
    assert r.unmuted


# Generated at 2022-06-14 08:08:28.146172
# Unit test for function mute
def test_mute():
    from .primitive import ArrayRegister
    from .primitive import ScalarRegister
    from .primitive import RegisterFile

    test_array_reg = ArrayRegister(8, 2, 'test_array_reg')
    test_scalar_reg = ScalarRegister(4, 'test_scalar_reg')
    test_scalar_reg_file = RegisterFile(2, 4, 'test_scalar_reg_file')

    mute(test_array_reg, test_scalar_reg, test_scalar_reg_file)

    assert test_array_reg._mute is True
    assert test_scalar_reg._mute is True
    assert test_scalar_reg_file._mute is True



# Generated at 2022-06-14 08:08:40.465077
# Unit test for function unmute
def test_unmute():
    class Register_Mock(Register):
        publ = 0
        
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.publ = kwargs['publ']
            
        def _get_mute(self) -> bool:
            return self.publ
            
        def _set_mute(self, mute: bool):
            self.publ = mute
    
    reg1 = Register_Mock(publ = True)
    reg2 = Register_Mock(publ = True)
    unmute(reg1, reg2)
    if not (reg1.publ and reg2.publ):
        sys.exit("Calling 'unmute(reg1, reg2)' didn't unmute both registers.")
    
    reg1 = Register_M

# Generated at 2022-06-14 08:08:48.087083
# Unit test for function mute
def test_mute():
    registers = [
        Register(name='a', width=16),
        Register(name='b', width=32),
        Register(name='c', width=64),
    ]

    for r in registers:
        r.unmute()
        assert r.absolute_mute == 0, '0 is unmuted'

    mute(*registers)

    for r in registers:
        assert r.absolute_mute == 1, '1 is muted'



# Generated at 2022-06-14 08:08:59.012080
# Unit test for function mute
def test_mute():
    from .primitive import DRegister
    reg0 = DRegister(name="reg0", bitwidth=16)
    reg1 = DRegister(name="reg1", bitwidth=12)
    reg0.wr_port.wr_data = 16
    reg1.wr_port.wr_data = 12

    reg0.wr_port.wr.value = 1
    reg1.wr_port.wr.value = 1

    reg0.wr_port.wr.value = 0
    reg1.wr_port.wr.value = 0

    assert reg0.rd_port.rd_data == 16
    assert reg1.rd_port.rd_data == 12

    mute(reg0, reg1)
    reg0.wr_port.wr_data = 10
    reg1.wr_port.wr_data = 8
    reg

# Generated at 2022-06-14 08:09:04.005437
# Unit test for function unmute
def test_unmute():
    from .primitive import Register

    reg = Register("test")
    unmute(reg)
    assert reg.is_muted() == False
    mute(reg)
    assert reg.is_muted() == True
    unmute(reg)
    assert reg.is_muted() == False



# Generated at 2022-06-14 08:09:12.635115
# Unit test for function mute
def test_mute():
    import numpy as np
    from .primitive import Bit

    # unit test for mute()
    b0 = Bit()
    b1 = Bit()
    mute(b0, b1)
    assert b0.muted == True
    assert b1.muted == True
    assert b0.value == np.nan
    assert b1.value == np.nan

    b0.set_value(1)
    b1.set_value(0)
    assert b0.value == np.nan
    assert b1.value == np.nan

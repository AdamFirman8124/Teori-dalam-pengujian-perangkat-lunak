

# Generated at 2022-06-14 08:07:53.328537
# Unit test for function unmute
def test_unmute():
    from .primitive import ByteRegister
    register_list = [ByteRegister() for _ in range(100)]
    try:
        mute(*register_list)
    except ValueError:
        raise
    assert all(reg.mute_state for reg in register_list)
    unmute(*register_list)
    assert not any(reg.mute_state for reg in register_list)



# Generated at 2022-06-14 08:08:05.887138
# Unit test for function unmute
def test_unmute():
    import unittest

    class Test(unittest.TestCase):
        def setUp(self):
            from .primitive import Register

            self.reg1 = Register()
            self.reg2 = Register()

            self.objs = (self.reg1, self.reg2)

        def test_unmute_noargs(self):
            reg1, reg2 = self.reg1, self.reg2

            reg1.mute()
            reg2.mute()

            unmute()

            self.assertFalse(any(reg1.mute_all), "Multiple registers unmuted")

        def test_unmute_noargs_exception(self):
            reg1, reg2 = self.reg1, self.reg2

            reg1.mute()
            reg2.mute()


# Generated at 2022-06-14 08:08:14.172733
# Unit test for function mute
def test_mute():
    import pytest
    from .primitive import Register
    
    reg_mute = Register()
    reg_not_mute = Register()
    reg_mute.mute()
    
    mute(reg_mute, reg_not_mute)
    
    assert reg_not_mute._mute == True
    assert reg_not_mute._mute == True
    
    with pytest.raises(ValueError):
        mute(1)


# Generated at 2022-06-14 08:08:21.365756
# Unit test for function unmute
def test_unmute():
    # Create a new register and then mute it
    r1 = Register(1, 'test_unmute1', 'test_unmute1.txt', 10)
    r1.mute()
    assert r1.get_muted()
    unmute(r1)
    assert not r1.get_muted()
    # Clean up
    del r1


# Generated at 2022-06-14 08:08:25.944220
# Unit test for function unmute
def test_unmute():
    test_data = [register_b, register_w, register_title]
    for reg in test_data:
        reg.unmute()
        for value in reg:
            assert value == reg._default_val

# Generated at 2022-06-14 08:08:32.021060
# Unit test for function unmute
def test_unmute():
    from .primitive import register, gate
    from .config import Configuration

    enable = gate()
    reg = register()
    mute(reg, enable)
    Configuration.enable_bitstream_optimization = True
    unmute(reg, enable)
    Configuration.enable_bitstream_optimization = False

# Generated at 2022-06-14 08:08:39.391204
# Unit test for function unmute
def test_unmute():
    class TestRegister(Register):
        def __init__(self: 'TestRegister', value: int) -> None:
            self.value = value
            self.muted = False

    a = TestRegister(1)
    mute(a)
    assert a.muted
    unmute(a)
    assert not a.muted

# Generated at 2022-06-14 08:08:52.252787
# Unit test for function unmute
def test_unmute():
    from .primitive import Register
    from .utils import TimeFormat
    from .flop import FlipFlop
    from .core import sim

    time_format = TimeFormat('ns')
    reg1 = Register('test1', width=8, format=time_format,
                    init_value=0x5)
    reg2 = Register('test2', width=8, format=time_format,
                    init_value=0x5)
    reg3 = Register('test3', width=8, format=time_format,
                    init_value=0x5)
    reg4 = Register('test4', width=8, format=time_format,
                    init_value=0x5)
    reg1.set_timeContext(time_format)
    reg2.set_timeContext(time_format)
    reg3.set_time

# Generated at 2022-06-14 08:08:58.753493
# Unit test for function mute
def test_mute():
    """
    This function tests the mute function against the same function
    in a class object.
    """
    class TestClass:
        def __init__(self):
            pass

        def mute(self) -> None:
            print('muted')

    obj = TestClass()
    mute(obj)



# Generated at 2022-06-14 08:09:06.010302
# Unit test for function mute
def test_mute():
	data = [0x07, 0x78]
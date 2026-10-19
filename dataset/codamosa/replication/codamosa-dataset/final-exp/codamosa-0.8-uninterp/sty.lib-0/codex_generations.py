

# Generated at 2022-06-14 08:07:53.026093
# Unit test for function mute
def test_mute():
    """
    Unit test for function mute.
    """
    reg = Register(
        name='test',
        address=0,
        width=8,
        mode='rw',
        poll_interval=0.01,
        write_only_on_change=False,
    )
    assert not reg.is_muted

    mute(reg)
    assert reg.is_muted

    unmute(reg)
    assert not reg.is_muted

# Generated at 2022-06-14 08:07:57.501376
# Unit test for function unmute
def test_unmute():
    from .system import System
    from .network import Network

    sys = System()
    net = Network()

    net.register(sys)
    net.mute(sys)

    assert sys._muted

    net.unmute(sys)

    assert not sys._muted

# Generated at 2022-06-14 08:08:01.276629
# Unit test for function unmute
def test_unmute():
    from .testobjects import register_objects
    registers = register_objects()
    mute(*registers)
    unmute(*registers)
    assert all(reg.muted == False for reg in registers)



# Generated at 2022-06-14 08:08:05.887859
# Unit test for function mute
def test_mute():
    """
    Testing the mute() function.
    """
    from .custom_types import BitArray
    reg = Register(BitArray(2), register_name="test_mute")
    reg.mute()
    assert reg.mute_flag == 1


# Generated at 2022-06-14 08:08:18.295544
# Unit test for function unmute
def test_unmute():
    from .primitive import RegBit
    reg1 = RegBit(name="reg1", width=4)
    reg2 = RegBit(name="reg2", width=4)
    reg3 = RegBit(name="reg3", width=4)
    reg4 = RegBit(name="reg4", width=4)
    reg5 = RegBit(name="reg5", width=4)

    mute(reg1, reg2, reg3, reg4, reg5)
    unmute(reg1, reg2)
    assert reg1.mute_counter == 0
    assert reg2.mute_counter == 0
    assert reg3.mute_counter == 1
    assert reg4.mute_counter == 1
    assert reg5.mute_counter == 1

# Generated at 2022-06-14 08:08:21.634919
# Unit test for function unmute
def test_unmute():
    class Test(Register):
        def __init__(self, name: str = "Test"):
            super().__init__(name)
            self.set_muted(True)
        def perform(self, *args, **kwargs):
            return
    test = Test()
    assert test.get_muted() == True
    unmute(test)
    assert test.get_muted() == False



# Generated at 2022-06-14 08:08:29.495176
# Unit test for function mute
def test_mute():
    """ Test function mute when called on a register-object """
    r0 = Register(0, "r0")
    r1 = Register(0, "r1")
    r2 = Register(0, "r2")
    r3 = Register(0, "r3")
    r4 = Register(0, "r4")
    mute(r0, r1, r2, r3, r4)
    for i in range(5):
        assert r0.muted



# Generated at 2022-06-14 08:08:34.355167
# Unit test for function mute
def test_mute():

    class TestRegisterClass(Register):
        def __init__(self): pass

    reg1 = TestRegisterClass()
    reg2 = TestRegisterClass()

    mute(reg1, reg2)

    assert reg1.muted
    assert reg2.muted



# Generated at 2022-06-14 08:08:37.034588
# Unit test for function mute
def test_mute():
    from .primitive import Register
    from .primitive import Part
    part = Part("test", 0, 0)
    reg = Register("test", 0, 0, part)
    mute(reg)
    assert reg.flags["muted"] == 1



# Generated at 2022-06-14 08:08:42.491107
# Unit test for function unmute
def test_unmute():
    ra = BasicRegister('register_a', 'rw', 0)
    rb = BasicRegister('register_b', 'rw', 0)
    mute(ra, rb)
    unmute(ra, rb)
    assert ra.is_muted==False
    assert rb.is_muted==False
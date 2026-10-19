

# Generated at 2022-06-14 08:07:57.325232
# Unit test for function unmute
def test_unmute():
    R1 = Register(muted=True, value=5, width=4)
    R2 = Register(muted=True, value=5, width=4)
    print(R1.muted, R2.muted)
    unmute(R1, R2)
    print(R1.muted, R2.muted)



# Generated at 2022-06-14 08:08:03.969826
# Unit test for function mute
def test_mute():
    from ..primitive import Bit
    from .primitive import Register, RegisterIter
    
    bit = Bit()
    register = Register(bit.mute, name="Test_register")
    register[0] = 1
    assert bit.state == 1, "Register test failed"
    register[0] = 1
    assert bit.state == 0, "Mute test failed"


# Generated at 2022-06-14 08:08:05.129497
# Unit test for function mute
def test_mute():
    pass



# Generated at 2022-06-14 08:08:12.378495
# Unit test for function mute
def test_mute():
    mute(vm.A, vm.E, vm.mem)
    assert vm.A.mute
    assert vm.E.mute
    assert vm.mem.mute
    mute(vm.A, vm.E, vm.mem)
    assert vm.A.mute
    assert vm.E.mute
    assert vm.mem.mute


# Generated at 2022-06-14 08:08:17.100519
# Unit test for function mute
def test_mute():
    reg1 = Register(name='reg1', width=32, stride=32)
    reg2 = Register(name='reg2', width=32, stride=32)
    mute(reg1, reg2)
    assert reg1.is_muted() and reg2.is_muted()



# Generated at 2022-06-14 08:08:19.597647
# Unit test for function mute
def test_mute():
    # Arrange
    b = Register(False)

    # Act
    mute(b)

    # Assert
    assert b in Register.muted



# Generated at 2022-06-14 08:08:29.586820
# Unit test for function unmute
def test_unmute():
    """
    Unit test for function unmute
    """
    err = ValueError(
        "The unmute() method can only be used with objects that inherit "
        "from the 'Register class'."
    )
    obj = Register(0, 'A', bits=8, description='Register for test')
    assert(isinstance(obj, Register))
    obj.mute()
    obj.unmute()

    try:
        unmute(0)
        assert(False)
    except ValueError as e:
        if not err.args == e.args:
            assert(False)

    try:
        unmute(0, 'A')
        assert(False)
    except ValueError as e:
        if not err.args == e.args:
            assert(False)


# Generated at 2022-06-14 08:08:32.559941
# Unit test for function unmute
def test_unmute():
    reg = Register(0x00)
    mute(reg)
    assert reg.is_muted()
    unmute(reg)
    assert not reg.is_muted()

# Generated at 2022-06-14 08:08:38.927835
# Unit test for function unmute
def test_unmute():
    x = Register(10)
    y = Register(20)
    z = Register(30)
    mute(x, y, z)
    unmute(x)
    assert x.read() == 10
    assert y.read() == 0
    assert z.read() == 0


# Generated at 2022-06-14 08:08:43.973866
# Unit test for function unmute
def test_unmute():
    a = unmute() == None
    b = unmute(0) == None
    c = unmute(0,1) == None
    d = unmute(None, '', [], {}) == None
    e = unmute(1j) == None
    return [a,b,c,d,e]

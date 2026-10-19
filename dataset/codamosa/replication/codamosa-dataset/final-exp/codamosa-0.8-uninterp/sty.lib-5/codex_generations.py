

# Generated at 2022-06-14 08:07:49.919185
# Unit test for function unmute
def test_unmute():
    from .primitive import Integer, Float, Boolean
    a = Integer()
    mute(a)
    assert a.muted == True
    unmute(a)
    assert a.muted == False

# Generated at 2022-06-14 08:07:55.827375
# Unit test for function unmute
def test_unmute():
    class A(Register):
        pass
    a = A(2)
    b = A(1)
    assert not a.muted and not b.muted
    mute(a, b)
    assert a.muted and b.muted
    unmute(a, b)
    assert not a.muted and not b.muted

# Generated at 2022-06-14 08:07:59.744066
# Unit test for function unmute
def test_unmute():
    """
    Test the function unmute()
    """
    import pytest

    reg = Register()
    unmute(reg)

    with pytest.raises(ValueError):
        unmute(0)

# Generated at 2022-06-14 08:08:03.865273
# Unit test for function mute
def test_mute():
    reg = Register(5)
    reg.value = 0b11111
    mute(reg)
    assert reg.value == 0b00000
    mute(reg)
    assert reg.value == 0b00000



# Generated at 2022-06-14 08:08:10.728325
# Unit test for function unmute
def test_unmute():
    # If objects are not register class objects
    obj = 'This is a string'
    with pytest.raises(ValueError):
        unmute(obj)

    # If objects are valid 
    reg1 = Register(initial_value=1)
    reg2 = Register(initial_value=2)
    unmute(reg1, reg2)



# Generated at 2022-06-14 08:08:16.385559
# Unit test for function unmute
def test_unmute():
    from .primitive import Reg16
    regs = [Reg16(i) for i in range(0, 10)]
    mute(*regs)
    assert all([reg.mute_state is True for reg in regs])
    unmute(*regs)
    assert all([reg.mute_state is False for reg in regs])

# Generated at 2022-06-14 08:08:23.089988
# Unit test for function mute
def test_mute():
    print("test_mute")
    r = Register()
    print("r = Register()")
    r.set(0)
    print("r.set(0)")
    r.mute()
    print("r.mute()")
    r.inc()
    print("r.inc()")
    print("Test passed!")


# Generated at 2022-06-14 08:08:31.014083
# Unit test for function unmute
def test_unmute():
    import random
    import pytest

    from .utils import parse_register_value

    register = Register(name="R1", bit_width=8, signed=True)
    values = list(range(-127, 128))
    expected_result = random.choice(values)

    register.write(expected_result)
    register.mute()
    register.unmute()
    result = register.read()

    assert parse_register_value(expected_result) == result



# Generated at 2022-06-14 08:08:42.277092
# Unit test for function unmute
def test_unmute():
    err = ValueError(
        "The unmute() method can only be used with objects that inherit "
        "from the 'Register class'."
    )
    reg_obj_1 = Register("test_1")
    reg_obj_2 = Register("test_2")
    reg_obj_3 = Register("test_3")
    reg_obj_4 = "Not a register object"
    mute(reg_obj_1, reg_obj_2, reg_obj_3)
    assert reg_obj_1.is_muted()
    assert reg_obj_2.is_muted()
    assert reg_obj_3.is_muted()
    unmute(reg_obj_1, reg_obj_2, reg_obj_3, reg_obj_4)
    assert not reg_obj_1.is_muted()

# Generated at 2022-06-14 08:08:43.259604
# Unit test for function mute
def test_mute():
    pass


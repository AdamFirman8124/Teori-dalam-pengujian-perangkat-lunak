

# Generated at 2022-06-14 08:08:00.781106
# Unit test for function mute
def test_mute():
    import pytest
    import pysyma.primitive as primitive
    reg0 = primitive.Register(name="test", size=3)
    reg1 = primitive.Register(name="test1", size=5)
    mute(reg0, reg1)
    assert all(obj.muted for obj in (reg0, reg1))
    unmute(reg0, reg1)
    assert all(not obj.muted for obj in (reg0, reg1))
    with pytest.raises(ValueError):
        mute("test")
        mute(3)
        mute(primitive.IMul(primitive.Register(name="test"), 4))



# Generated at 2022-06-14 08:08:06.291251
# Unit test for function mute
def test_mute():
    from .primitive import Register, Mapping

    mapped = Register(0x2)
    r = Register(4, name='test', mapping=Mapping(mapped, 1, 5))

    mute(r)
    assert r.muted is True

    unmute(r)
    assert r.muted is False


# Generated at 2022-06-14 08:08:18.989896
# Unit test for function unmute
def test_unmute():
    """
    Test for the unmute() function.
    """
    from .primitive import Register
    from .bit import Bit

    # Initialize objects
    err = ValueError(
        "The unmute() method can only be used with objects that inherit "
        "from the 'Register class'."
    )

    # Test with non-Register objects
    obj = 2
    try:
        unmute(obj)
        raise AssertionError("unmute() should raise an error with non-Register "
                             "objects")
    except ValueError as e:
        assert err in str(e)

    # Test with Register object
    obj = Register("Obj")
    unmute(obj)
    assert obj._muted is False
    assert obj._muted_value is None

    # Test with nested objects
    obj = Register("Obj")


# Generated at 2022-06-14 08:08:29.340434
# Unit test for function mute
def test_mute():
    reg1 = Register(1, nbits=16, dtype=np.uint8,
                    init_st='zero', init_val=0,
                    st_names=None, st_values=None,
                    cont_st=False, enum_out=False,
                    enum_out_labels=None,
                    low_lvl_st=False,
                    fxn_next=None, fxn_out=None,
                    scope=None, label=None)


# Generated at 2022-06-14 08:08:34.876203
# Unit test for function mute
def test_mute():
    reg_1 = Register(0)
    reg_2 = Register(0)
    reg_3 = Register(0)
    mute(reg_1, reg_2, reg_3)

    assert reg_1._muted
    assert reg_2._muted
    assert reg_3._muted



# Generated at 2022-06-14 08:08:37.318776
# Unit test for function unmute
def test_unmute():
    dut = Register(0)
    dut.mute()
    dut.unmute()
    assert dut.muted == False



# Generated at 2022-06-14 08:08:42.527518
# Unit test for function mute
def test_mute():
    # Define registers
    class DUT(Register):
        reg1: int
        reg2: int
        reg3: int

    # Call function
    mute(DUT.reg1, DUT.reg2)

    # Check function
    assert DUT.reg1.muted is True
    assert DUT.reg2.muted is True
    assert DUT.reg3.muted is False



# Generated at 2022-06-14 08:08:55.838435
# Unit test for function mute
def test_mute():
    from .primitive import Bit, Mux, Wire, Dff


# Generated at 2022-06-14 08:09:07.144491
# Unit test for function unmute
def test_unmute():
    """
    Example how to use the unmute() function. This test calls for the unmute() function and checks the
    expected output is equal to the actual output.
    """
    import pytest
    from .primitive import boolean_register
    from .primitive import integer_register

    b_reg1 = boolean_register("b_reg1")
    b_reg2 = boolean_register("b_reg2")
    i_reg1 = integer_register("i_reg1")
    i_reg2 = integer_register("i_reg2")
    unmute(b_reg1)
    unmute(b_reg2)
    unmute(i_reg1)
    unmute(i_reg2)
    assert b_reg1.is_mute() == False
    assert b_reg2.is_mute() == False

# Generated at 2022-06-14 08:09:11.047433
# Unit test for function mute
def test_mute():
    """
    Test of the mute() function.
    """
    class TestClass(Register):
        def __init__(self):
            Register.__init__(self)

    mute(TestClass())

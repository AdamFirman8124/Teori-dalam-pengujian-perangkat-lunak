

# Generated at 2022-06-14 08:07:58.450024
# Unit test for function unmute
def test_unmute():
    """ Test the mute() and unmute() functions. """
    r1 = Register(False, "R1")
    assert r1.mute(r1) == r1
    assert r1.unmute(r1) == r1

    r1 = Register(False, "R1")
    assert r1.mute(r1, r1) == r1
    assert r1.unmute(r1, r1) == r1

    r1 = Register(False, "R1")
    assert r1.mute(r1, r1, r1) == r1
    assert r1.unmute(r1, r1, r1) == r1

    r1, r2 = Register(False, "R1"), Register(False, "R2")

# Generated at 2022-06-14 08:08:05.836024
# Unit test for function mute
def test_mute():
    # Create a test-register
    reg = Register(
        name='reg1',
        address=0x01
    )
    # Activate the test-register
    reg.enable()
    # Check if the test-register is enabled
    assert reg.enabled == True
    # Mute the test-register
    mute(reg)
    # Check if the test-register is muted
    assert reg.muted == True



# Generated at 2022-06-14 08:08:12.728464
# Unit test for function unmute
def test_unmute():
    from main import Unmute
    from .primitive import Register
    from .framework import Object, Union

    class Test(Object):
        a: Register()
        b: Union(a)

    t = Test()
    unmute(t.a, t.b)
    assert t.a.muted == False
    assert t.b.muted == False



# Generated at 2022-06-14 08:08:15.242278
# Unit test for function unmute
def test_unmute():
    a = Register('a')
    mute(a)

    unmute(a)

    assert_equal(a.unmute(), a)

# Generated at 2022-06-14 08:08:27.669771
# Unit test for function mute
def test_mute():
    from .pwm import PWM
    from .pin import Pin
    pin_A = Pin(0)
    pwm_A = PWM(pin_A)
    pin_B = Pin(1)
    pwm_B = PWM(pin_B)
    pin_C = Pin(2)
    pwm_C = PWM(pin_C)
    pin_D = Pin(3)
    pwm_D = PWM(pin_D)

    print("original:")
    print(pwm_A.is_muted(), pwm_B.is_muted(), pwm_C.is_muted(), pwm_D.is_muted())
    mute(pwm_A, pwm_B, pwm_C)
    print("muted:")

# Generated at 2022-06-14 08:08:40.166209
# Unit test for function unmute
def test_unmute():
    # import modules
    import numpy as np
    import random

    # Create a register, fill it with random values and mute it
    reg = Register(np.random.random(10))
    reg.mute()

    # Create an unmutex, fill it with random values and unmute it
    unmutex = Register(np.random.random(9))
    unmute(unmutex)

    # Check if the new created unmutex is really unmuted
    assert np.array_equal(unmutex.get(), unmutex.get())

    # Try to unmute the original muted register, unmute only works
    # with unmuted registers
    try:
        unmute(reg)
    except ValueError:
        reg_was_unmuted = False
    else:
        reg_was_unmuted = True

# Generated at 2022-06-14 08:08:52.263567
# Unit test for function mute
def test_mute():
    """
    Test umute function from module function.py

    :return: Nothing
    """
    from .primitive import Register
    from .component import Memory, RegisterFile

    # Create a register file.
    regfile = RegisterFile(8, 32, "rf")
    for i in range(8):
        regfile.write(i, "w{}".format(i))

    # Create a memory.
    mem = Memory(8, 32, "mem")
    for i in range(8):
        mem.write(i, "w{}".format(i))

    # Create a register.
    reg = Register(32, "reg")
    reg.mux_data(regfile, mem, 0)
    reg.set_selector_value(0)

    # Mute the objects.

# Generated at 2022-06-14 08:09:02.936691
# Unit test for function unmute
def test_unmute():
    class TestRegister(Register):
        def __init__(self):
            self.muted = False

        def mute(self):
            self.muted = True

        def unmute(self):
            self.muted = False

        def is_muted(self):
            return self.muted

    reg = TestRegister()
    assert not reg.is_muted()
    mute(reg)
    assert reg.is_muted()
    unmute(reg)
    assert not reg.is_muted()
    unmute(reg)
    assert not reg.is_muted()


# Generated at 2022-06-14 08:09:11.657346
# Unit test for function unmute
def test_unmute():
    a = Register()
    b = Register()

    a(1)
    b(2)

    assert a.read() == 1
    assert b.read() == 2

    mute(a, b)

    a(10)
    b(20)

    assert a.read() == None
    assert b.read() == None

    unmute(a, b)

    a(100)
    b(200)

    assert a.read() == 100
    assert b.read() == 200


if __name__ == "__main__":
    test_unmute()

# Generated at 2022-06-14 08:09:23.715074
# Unit test for function mute
def test_mute():
    from .register import Register16
    from .gates import Xor
    from .bus import Wire
    from .primitive import Mux, Adder, Incrementor

    a = Register16(name="a")
    b = Register16(name="b")

    s = Wire()
    c = Wire()
    adder_out = Wire()
    reg_adders = [Wire() for _ in range(16)]

    Xor(s, a.mux_sel, b.mux_sel)

    mux_a = Mux(a.out, a.in_, s)
    mux_b = Mux(b.out, b.in_, s)

    Adder(adder_out, mux_a, mux_b, c)
    adder_out.connect(a.in_, c)


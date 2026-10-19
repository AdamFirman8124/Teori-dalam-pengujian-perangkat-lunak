

# Generated at 2022-06-14 08:08:01.983609
# Unit test for function unmute
def test_unmute():
    from .primitive import uint4, uint12
    from .compound import dff
    import magma as m
    m.set_mantle_target("ice40")

    reg = m.DefineRegister(uint4, init=0)
    d = dff(reg)()
    d[0].unmute()
    d[0].mute()
    d[0].unmute()

    d[0].data = 7
    tester = m.Tester(d, d.clk)
    tester.eval()
    tester.step(2)
    tester.print("Output:")
    tester.print(d.O)
    tester.compile_and_run("verilator", flags=["-Wno-fatal"])



# Generated at 2022-06-14 08:08:06.847445
# Unit test for function unmute
def test_unmute():
    from .primitive import Register
    from . import ahb
    r = Register(ahb)
    # This is just for testing - normally a register would be
    # instantiated with a module/bus.
    r.mute()
    unmute(r)
    assert r.muted == False



# Generated at 2022-06-14 08:08:12.728195
# Unit test for function mute
def test_mute():
    r1 = Register(1)
    r2 = Register(0)
    r1.mute()
    r2.mute()
    assert r1.log.empty()
    assert r2.log.empty()
    assert r1.get() == 1
    assert r2.get() == 0

# Generated at 2022-06-14 08:08:19.171048
# Unit test for function mute
def test_mute():
    reg1: Register = Register(0)
    reg2: Register = Register(1)
    assert reg1.value == 0
    assert reg2.value == 1
    mute(reg1, reg2)
    reg1.increment()
    reg2.increment()
    assert reg1.value == 0
    assert reg2.value == 1



# Generated at 2022-06-14 08:08:29.424880
# Unit test for function mute
def test_mute():
    dut.a.set(0x10)
    dut.b.set(0xFF)
    dut.mux = 0
    dut.load = 1
    dut.oin = 1
    hf.delay_us(20)
    dut.load = 0
    hf.delay_us(20)
    dut.oin = 0
    dut.mux = 1
    hf.delay_us(20)
    dut.load = 1
    hf.delay_us(20)
    dut.load = 0
    hf.delay_us(20)
    dut.mux = 0
    a, b = dut.a.get(), dut.b.get()
    assert dut.a.value == 0x10
    assert dut.b.value == 0

# Generated at 2022-06-14 08:08:35.470241
# Unit test for function unmute
def test_unmute():
    from .primitive import D
    d = D()
    mute(d)
    n = 0
    for x in d:
        n += 1
        if n > 10:
            break
    unmute(d)
    n = 0
    for x in d:
        n += 1
    assert n==10
    d.unmute()
    n = 0
    for x in d:
        n += 1
    assert n==11


# Generated at 2022-06-14 08:08:41.532449
# Unit test for function unmute
def test_unmute():
    """
    Unit test for function unmute.
    """
    a = Register("a", __debug__ = False)
    mute(a)
    assert a.is_muted()
    unmute(a)
    assert not a.is_muted()


# Generated at 2022-06-14 08:08:50.670068
# Unit test for function unmute
def test_unmute():
    # Suppress console output for unit test
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w')

    # Create a register
    instance = Register(
        clock=Clock(),
        bit_width=8,
        name='test_register'
    )

    # Call the function
    unmute(instance)

    # Assert that the register is unmuted
    assert instance.muted is False

    # Close the stdout stream
    sys.stdout.close()
    sys.stderr.close()


# Generated at 2022-06-14 08:08:54.419682
# Unit test for function mute
def test_mute():
    """
    Tests the mute() function.
    """
    A = Register(8)
    B = Register(8)
    C = Register(8)
    mute(A, B, C)
    assert A.is_muted()
    assert B.is_muted()
    assert C.is_muted()



# Generated at 2022-06-14 08:08:56.655079
# Unit test for function unmute
def test_unmute():
    stub = True
    assert stub, "test unit-test"
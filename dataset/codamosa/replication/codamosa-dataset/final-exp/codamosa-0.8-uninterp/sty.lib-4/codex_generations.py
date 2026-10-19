

# Generated at 2022-06-14 08:07:52.828986
# Unit test for function mute
def test_mute():
    mute(register_1, register_2, register_3)
    assert register_1._muted is True
    assert register_2._muted is True
    assert register_3._muted is True


# Generated at 2022-06-14 08:08:04.275055
# Unit test for function unmute
def test_unmute():
    """This is a unit test for the unmute method."""
    import nmrglue as ng
    import numpy as np
    from pynmrstar import loop, Entry
    from nmrstarlib.util_ import iter_as_list
    d = ng.pipe.read("common_data/3d/NmrPipe/test.fid")
    par = ng.pipe.read_pars("common_data/3d/NmrPipe/test.fid")
    udic = ng.pipe.guess_udic(dic, d)
    star = ng.pipe.make_uc(d, par, udic)
    entry = Entry.from_object(star)
    loop_obj = loop.Loop.from_object(lic=entry["_Spectral_Peak_list"])
    assert np

# Generated at 2022-06-14 08:08:17.518699
# Unit test for function mute
def test_mute():
    from .extended import Worker, Job, Job_eihi, Job_eio, Job_iohe

    @Worker()
    class Worker1:
        @Job(1)
        def first(self):
            return 0

    w1 = Worker1(1)
    mute(w1.first)
    assert len(w1.first.job_queue) == 0
    assert len(w1.first.error_registry) == 0

    @Worker()
    class Worker2:
        @Job_eihi(1, 2)
        def first(self):
            return 0

    w2 = Worker2(1)
    mute(w2.first)
    assert len(w2.first.job_queue) == 0
    assert len(w2.first.error_registry) == 0


# Generated at 2022-06-14 08:08:27.093786
# Unit test for function unmute
def test_unmute():

    a = Register("a")
    b = Register("b", size=4)
    c = Register("c")

    mute(a, b, c)

    assert a.mute_count == 1
    assert b.mute_count == 1
    assert c.mute_count == 1

    unmute(a, c)

    assert a.mute_count == 0
    assert c.mute_count == 0

    with pytest.raises(ValueError):
        mute(1)
        unmute(1)
        mute(a, 1)
        unmute(a, 1)

# Generated at 2022-06-14 08:08:35.249667
# Unit test for function mute
def test_mute():
    a = Register(0x01, size=8)
    b = Register(0x02, size=8)
    c = Register(0x03, size=8)
    mute(a, b, c)
    assert a.mutecount==1, "Mute function didn't work"
    assert b.mutecount==1, "Mute function didn't work"
    assert c.mutecount==1, "Mute function didn't work"


# Generated at 2022-06-14 08:08:43.162553
# Unit test for function unmute
def test_unmute():
    R1 = Register("R1",6)
    R2 = Register("R2",6)
    R3 = Register("R3",6)
    R4 = Register("R4",6)
    R1.mute()
    R2.mute()
    R3.mute()
    R4.mute()
    unmute(R1,R2,R3,R4)
    assert R1.is_muted() == False
    assert R2.is_muted() == False
    assert R3.is_muted() == False
    assert R4.is_muted() == False


# Generated at 2022-06-14 08:08:50.204709
# Unit test for function unmute
def test_unmute():
    from .primitive import Bit
    from .primitive import Byte
    from .primitive import Register
    from .primitive import Nibble
    from .primitive import Word

    a = Bit()
    b = Byte()
    c = Nibble()
    d = Word()
    
    mute(a, b, c, d)
    unmute(a, b, c, d)

# Generated at 2022-06-14 08:08:58.599163
# Unit test for function mute
def test_mute():

    r1 = Register("r1", -5, 4)
    r2 = Register("r2", -5, 4)
    r3 = Register("r3", -5, 4)
    r4 = Register("r4", -5, 4)

    mute(r1, r3)
    for reg in [r1, r2, r3, r4]:
        assert reg.is_muted

    unmute(r2, r4)
    assert r1.is_muted
    assert not r2.is_muted
    assert r3.is_muted
    assert not r4.is_muted

# Generated at 2022-06-14 08:09:07.112884
# Unit test for function unmute
def test_unmute():
    from .primitive import Register
    from .devices import SysADC
    from .gateware import Mux
    from .templates import register_map
    from .controller import Controller, run_sequence

    adc_channels = Mux
    adc_channel_names = ['voltage']
    adc_channel_mux = adc_channels(channel_names=adc_channel_names)
    adc = SysADC()
    with Controller(register_map) as ctrl:
        with adc.record(ctrl):
            run_sequence(ctrl)

# Generated at 2022-06-14 08:09:17.345707
# Unit test for function unmute
def test_unmute():
    import unittest
    import ikapati.primitive as prim

    class TestRegister(prim.Register):
        def __init__(self, name: str):
            super(TestRegister, self).__init__(name)

    class TestUnmute(unittest.TestCase):
        def setUp(self):
            self.reg1 = TestRegister('test reg 1')
            self.reg2 = TestRegister('test reg 2')
            self.reg3 = TestRegister('test reg 3')

        def test_unmute(self):
            mute(self.reg1, self.reg2)
            unmute(self.reg1)
            self.assertEqual(self.reg1.muted, False)
            self.assertEqual(self.reg2.muted, True)

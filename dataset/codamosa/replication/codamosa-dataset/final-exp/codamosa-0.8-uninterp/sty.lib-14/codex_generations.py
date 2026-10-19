

# Generated at 2022-06-14 08:07:56.447322
# Unit test for function unmute
def test_unmute():
    """
    This function tests the unmute function.
    """
    from ..primitive.data import Boolean
    from .register import Register
    from ..utility.enums import Direction

    reg = Register(Boolean(True, direction=Direction.OUT), name="MyRegister")
    reg.mute()
    assert reg.muted is True, "Register was muted"
    unmute(reg)
    assert reg.muted is False, "Register was unmuted"

# Generated at 2022-06-14 08:08:04.794643
# Unit test for function unmute
def test_unmute():
    """
    Tests the unmute function.
    """
    # create objects of the class 'Register'
    r1 = Register(3)
    r2 = Register(3)
    # mute the objects
    mute(r1, r2)
    # unmute the objects
    unmute(r1, r2)
    # test if the objects are not muted
    assert r1.is_muted() == False
    assert r2.is_muted() == False
    # expected output
    assert r1.output == '000'
    assert r2.output == '000'


# Generated at 2022-06-14 08:08:09.089929
# Unit test for function mute
def test_mute():
    """Function unit test"""
    test_register = Register("0", "0", "A")
    test_register.mute()
    assert test_register.is_muted is True


# Generated at 2022-06-14 08:08:14.061343
# Unit test for function unmute
def test_unmute():
    xp = xpdict(shm=False)
    n = xp["n"]
    n.q = 1
    n.mute()
    n.q = 2
    assert n.q == 1
    unmute(n)
    assert n.q == 2


# Generated at 2022-06-14 08:08:22.767167
# Unit test for function mute
def test_mute():
    def test_mute_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except ValueError as e:
                pass

            mute(pin14, pin15)

            assert pin14.muted == True
            assert pin15.muted == True

            unmute(pin14, pin15)

            assert pin14.muted == False

# Generated at 2022-06-14 08:08:28.014447
# Unit test for function mute
def test_mute():
    a = Register(name='test')
    b = Register(name='test_2')

    mute(a, b)
    assert a.muted
    assert b.muted

    unmute(a, b)
    assert not a.muted
    assert not b.muted

# Generated at 2022-06-14 08:08:32.130290
# Unit test for function unmute
def test_unmute():
    register = Register(8)
    register.mute()
    register.write(0xff)
    assert register.read() == 0
    unmute(register)
    assert register.read() == 0xff


# Generated at 2022-06-14 08:08:35.970134
# Unit test for function unmute
def test_unmute():
    r = Register(0)
    mute(r)
    assert r.muted
    unmute(r)
    assert not r.muted

# Test function mute

# Generated at 2022-06-14 08:08:49.301745
# Unit test for function unmute
def test_unmute():
    class TestObj(Register):
        def __init__(self, name: str, start: int, end: int):
            super().__init__(name, start, end)
            self._muted = False

        def mute(self):
            self._muted = True

        def unmute(self):
            self._muted = False

        @property
        def muted(self) -> bool:
            return self._muted

    obj1 = TestObj("test1", 0, 1)
    obj2 = TestObj("test2", 2, 3)
    obj3 = TestObj("test3", 4, 5)
    obj3._muted = True
    obj2._muted = True
    assert obj1.muted == False
    assert obj2.muted == True
    assert obj3.muted == True
    unmute

# Generated at 2022-06-14 08:08:57.211319
# Unit test for function unmute
def test_unmute():
    class Object(Register):
        def __init__(self):
            super().__init__(2, "Object")
            self.isMuted = False

        def mute(self):
            self.isMuted = True

        def unmute(self):
            self.isMuted = True

    obj = Object()

    assert obj.isMuted is False
    mute(obj)
    assert obj.isMuted is True
    unmute(obj)
    assert obj.isMuted is False
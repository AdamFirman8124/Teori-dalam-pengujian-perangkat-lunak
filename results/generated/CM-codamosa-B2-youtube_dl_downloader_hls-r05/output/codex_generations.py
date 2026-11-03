

# Generated at 2026-11-02 00:51:17.756538
# Unit test for constructor of class HlsFD
def test_HlsFD():
    class FakeYDL(object):
        pass

    fd = HlsFD(FakeYDL(), {})
    assert isinstance(fd, HlsFD)
    assert fd.FD_NAME == 'hlsnative'
    assert fd.ydl is not None
    assert fd.params == {}
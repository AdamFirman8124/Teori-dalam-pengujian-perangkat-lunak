

# Generated at 2026-11-03 03:15:16.933656
# Unit test for constructor of class _ScopeDict
def test__ScopeDict():
    class _FakeAVMClass(object):
        name = 'TestAVMClass'

    avm_class = _FakeAVMClass()
    scope_dict = _ScopeDict(avm_class)

    # Constructor should store the avm_class and behave like a dict
    assert isinstance(scope_dict, dict)
    assert scope_dict.avm_class is avm_class
    assert scope_dict.avm_class.name == 'TestAVMClass'
    assert len(scope_dict) == 0
    assert repr(scope_dict) == 'TestAVMClass__Scope({})'

    # Regular dict behaviour still works
    scope_dict['x'] = 1
    scope_dict['y'] = 2
    assert scope_dict['x'] == 1
    assert scope_dict['y'] == 2
    assert len(scope_dict) == 2
    assert 'x' in scope_dict
    del scope_dict['x']
    assert 'x' not in scope_dict
    assert len(scope_dict) == 1

# Generated at 2026-11-03 03:15:49.195574
# Unit test for method __repr__ of class _Multiname
def test__Multiname___repr__():
    from youtube_dl.swfinterp import _Multiname

    multiname = _Multiname(0)
    assert repr(multiname) == '[MULTINAME kind: 0x0]'

    multiname = _Multiname(0x1a)
    assert repr(multiname) == '[MULTINAME kind: 0x1a]'

    multiname = _Multiname(255)
    assert repr(multiname) == '[MULTINAME kind: 0xff]'

    multiname = _Multiname(0x0a)
    assert str(multiname) == '[MULTINAME kind: 0xa]'

# Generated at 2026-11-03 03:16:21.766918
# Unit test for method __bool__ of class _Undefined
def test__Undefined___bool__():
    from youtube_dl.swfinterp import _Undefined
    instance = _Undefined()
    assert instance.__bool__() is False
    assert instance.__nonzero__() is False
    assert not bool(instance)

# Generated at 2026-11-03 03:16:40.300145
# Unit test for method __bool__ of class _Undefined
def test__Undefined___bool__():
    u = _Undefined()
    assert u.__bool__() is False
    assert bool(u) is False
    assert not u

# Generated at 2026-11-03 03:19:23.014927
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-11-03 03:23:30.818967
# Unit test for method extract_class of class SWFInterpreter
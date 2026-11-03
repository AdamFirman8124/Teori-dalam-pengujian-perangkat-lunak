

# Generated at 2026-11-01 20:14:15.221446
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-11-01 20:15:37.652616
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-11-01 20:16:32.551203
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-11-01 20:17:09.497657
# Unit test for method __repr__ of class _Multiname
def test__Multiname___repr__():
    multiname = _Multiname(0x07)
    assert multiname.__repr__() == '[MULTINAME kind: 0x7]'

    multiname = _Multiname(0x0A)
    assert multiname.__repr__() == '[MULTINAME kind: 0xa]'

    multiname = _Multiname(0)
    assert multiname.__repr__() == '[MULTINAME kind: 0x0]'

# Generated at 2026-11-01 20:17:46.158260
# Unit test for method make_object of class _AVMClass
def test__AVMClass_make_object():
    # nonce:af53530e
    avm_class = _AVMClass(42, 'SampleClass')

    obj = avm_class.make_object()
    assert isinstance(obj, _AVMClass_Object)
    assert obj.avm_class is avm_class

    # Each call must produce a distinct object bound to the same class
    obj2 = avm_class.make_object()
    assert isinstance(obj2, _AVMClass_Object)
    assert obj2 is not obj
    assert obj2.avm_class is avm_class

    # repr should contain the class name and a hex id
    assert repr(obj).startswith('SampleClass#')
    assert repr(obj2).startswith('SampleClass#')
    assert repr(obj) != repr(obj2)

# Generated at 2026-11-01 20:19:34.200438
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-11-01 20:21:33.495793
# Unit test for method extract_function of class SWFInterpreter
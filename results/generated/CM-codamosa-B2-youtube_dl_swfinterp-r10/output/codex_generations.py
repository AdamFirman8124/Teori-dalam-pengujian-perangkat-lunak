

# Generated at 2026-11-01 22:11:13.983431
# Unit test for constructor of class _Multiname
def test__Multiname():
    mn = _Multiname(0x07)
    assert isinstance(mn, _Multiname)
    assert mn.kind == 0x07
    assert repr(mn) == '[MULTINAME kind: 0x7]'

    mn2 = _Multiname(0x1f)
    assert mn2.kind == 0x1f
    assert repr(mn2) == '[MULTINAME kind: 0x1f]'

# Generated at 2026-11-01 22:12:48.297600
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-11-01 22:14:35.055420
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-11-01 22:16:21.587379
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-11-01 22:17:12.315693
# Unit test for constructor of class _AVMClass
def test__AVMClass():
    # Basic construction without static properties
    avm_class = _AVMClass(name_idx=42, name='SomeClass')
    assert avm_class.name_idx == 42
    assert avm_class.name == 'SomeClass'
    assert avm_class.method_names == {}
    assert avm_class.method_idxs == {}
    assert avm_class.methods == {}
    assert avm_class.method_pyfunctions == {}
    assert avm_class.static_properties == {}
    assert avm_class.constants == {}

    # variables is a _ScopeDict bound to this class
    assert isinstance(avm_class.variables, _ScopeDict)
    assert avm_class.variables.avm_class is avm_class
    assert avm_class.variables == {}

    # Construction with static properties
    static_props = {'answer': 42}
    avm_class2 = _AVMClass(name_idx=1, name='OtherClass',
                           static_properties=static_props)
    assert avm_class2.static_properties == static_props

    # Falsy static_properties falls back to a new empty dict
    avm_class3 = _AVMClass(name_idx=2, name='ThirdClass', static_properties={})
    assert avm_class3.static_properties == {}
    assert avm_class3.static_properties is not None

    # repr
    assert repr(avm_class) == '_AVMClass(SomeClass)'

    # make_object returns an object tied to this class
    obj = avm_class.make_object()
    assert isinstance(obj, _AVMClass_Object)
    assert obj.avm_class is avm_class
    assert repr(obj).startswith('SomeClass#')

    # register_methods populates both name -> idx and idx -> name maps
    avm_class.register_methods({'methodA': 1, 'methodB': 2})
    assert avm_class.method_names == {'methodA': 1, 'methodB': 2}
    assert avm_class.method_idxs == {1: 'methodA', 2: 'methodB'}

    # register_methods merges with existing entries
    avm_class.register_methods({'methodC': 3})
    assert avm_class.method_names == {'methodA': 1, 'methodB': 2, 'methodC': 3}
    assert avm_class.method_idxs == {1: 'methodA', 2: 'methodB', 3: 'methodC'}

# Generated at 2026-11-01 22:19:31.955075
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from youtube_dl.swfinterp import SWFInterpreter, _AVMClass

    # Build an interpreter instance without running the SWF parser
    interpreter = object.__new__(SWFInterpreter)

    # Create a minimal AVM class
    avm_class = _AVMClass(0, 'PatchedClass')

    def original(args):
        return 'original'

    def replacement(args):
        return 'patched:%s' % (args[0],)

    # Seed the class with an existing implementation
    avm_class.method_pyfunctions['getValue'] = original

    # Patching an existing function must replace its entry
    interpreter.patch_function(avm_class, 'getValue', replacement)
    assert avm_class.method_pyfunctions['getValue'] is replacement
    assert avm_class.method_pyfunctions['getValue']([123]) == 'patched:123'

    # Patching a previously unknown function must register it
    interpreter.patch_function(avm_class, 'brandNew', replacement)
    assert avm_class.method_pyfunctions['brandNew'] is replacement
    assert avm_class.method_pyfunctions['brandNew'](['x']) == 'patched:x'

    # The original function object must remain untouched
    assert original([1]) == 'original'

    # Patching another class must not affect this one
    other_class = _AVMClass(1, 'OtherClass')
    interpreter.patch_function(other_class, 'getValue', original)
    assert other_class.method_pyfunctions['getValue'] is original
    assert avm_class.method_pyfunctions['getValue'] is replacement
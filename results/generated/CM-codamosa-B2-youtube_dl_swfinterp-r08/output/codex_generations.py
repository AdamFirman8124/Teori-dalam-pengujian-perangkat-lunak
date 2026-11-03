

# Generated at 2026-11-02 07:51:15.875738
# Unit test for method make_object of class _AVMClass
def test__AVMClass_make_object():
    avm_class = _AVMClass(42, 'TestAVMClass')
    obj = avm_class.make_object()

    # Returned object should be an _AVMClass_Object bound to the class
    assert isinstance(obj, _AVMClass_Object)
    assert obj.avm_class is avm_class
    assert obj.avm_class.name == 'TestAVMClass'

    # repr format: '<class name>#<id>'
    assert repr(obj) == 'TestAVMClass#%x' % id(obj)

    # Repeated calls should yield distinct objects tied to the same class
    obj2 = avm_class.make_object()
    assert obj2 is not obj
    assert obj2.avm_class is avm_class
    assert repr(obj2) == 'TestAVMClass#%x' % id(obj2)

# Generated at 2026-11-02 07:51:27.958033
# Unit test for method __repr__ of class _AVMClass
def test__AVMClass___repr__():
    avm_class = _AVMClass(1, 'TestClassName')
    assert repr(avm_class) == '_AVMClass(TestClassName)'

    avm_class2 = _AVMClass(42, 'flash.display.Sprite')
    assert repr(avm_class2) == '_AVMClass(flash.display.Sprite)'

    avm_class3 = _AVMClass(0, '')
    assert repr(avm_class3) == '_AVMClass()'

# Generated at 2026-11-02 07:51:55.920105
# Unit test for method __repr__ of class _AVMClass_Object
def test__AVMClass_Object___repr__():
    class FakeAVMClass(object):
        def __init__(self, name):
            self.name = name

    avm_class = FakeAVMClass('TestClassName')
    obj = _AVMClass_Object(avm_class)

    # repr should be "<class name>#<hex id>"
    expected = '%s#%x' % ('TestClassName', id(obj))
    assert repr(obj) == expected, (
        'Expected %r, got %r' % (expected, repr(obj)))

    # The repr should contain the class name
    assert 'TestClassName' in repr(obj)

    # A '#' separator should separate name from id
    assert repr(obj).startswith('TestClassName#')

    # Different instances should produce different ids in their reprs
    obj2 = _AVMClass_Object(avm_class)
    assert repr(obj2) == 'TestClassName#%x' % id(obj2)
    assert repr(obj) != repr(obj2)

# Generated at 2026-11-02 07:52:14.651581
# Unit test for constructor of class _AVMClass_Object
def test__AVMClass_Object():
    class _FakeAVMClass(object):
        def __init__(self, name):
            self.name = name

    avm_class = _FakeAVMClass('TestAVMClass')
    obj = _AVMClass_Object(avm_class)

    # Constructor must store the given avm_class
    assert obj.avm_class is avm_class

    # repr relies on the stored avm_class name and the object's id
    assert repr(obj) == 'TestAVMClass#%x' % id(obj)

    # A second instance keeps its own independent reference
    other_class = _FakeAVMClass('OtherAVMClass')
    other_obj = _AVMClass_Object(other_class)
    assert other_obj.avm_class is other_class
    assert other_obj.avm_class is not avm_class
    assert other_obj.avm_class.name == 'OtherAVMClass'
    assert repr(other_obj) == 'OtherAVMClass#%x' % id(other_obj)
    assert repr(other_obj) != repr(obj)

# Generated at 2026-11-02 07:53:02.058138
# Unit test for constructor of class _ScopeDict
def test__ScopeDict():
    class FakeAVMClass(object):
        def __init__(self, name):
            self.name = name

    avm_class = FakeAVMClass('SomeClass')
    scope = _ScopeDict(avm_class)

    # Constructor should initialize an empty dict and store the avm_class
    assert isinstance(scope, dict)
    assert len(scope) == 0
    assert scope.avm_class is avm_class
    assert scope.avm_class.name == 'SomeClass'

    # Regular dict behavior must still work
    scope['x'] = 1
    scope['y'] = 2
    assert scope['x'] == 1
    assert scope.get('z') is None
    assert sorted(scope.keys()) == ['x', 'y']
    del scope['x']
    assert list(scope.keys()) == ['y']

    # __repr__ should prefix the avm class name to the underlying dict repr
    assert repr(scope) == 'SomeClass__Scope(%s)' % dict.__repr__(scope)

    # Instances must not share state
    other = _ScopeDict(FakeAVMClass('OtherClass'))
    assert len(other) == 0
    assert other.avm_class is not avm_class
    assert repr(other) == 'OtherClass__Scope(%s)' % dict.__repr__(other)

# Generated at 2026-11-02 07:56:05.570570
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-11-02 07:58:32.870987
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-11-02 07:59:50.209564
# Unit test for constructor of class SWFInterpreter
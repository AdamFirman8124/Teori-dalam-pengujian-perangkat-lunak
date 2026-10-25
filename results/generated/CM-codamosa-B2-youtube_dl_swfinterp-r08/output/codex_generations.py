

# Generated at 2026-10-24 06:10:50.488130
# Unit test for method make_object of class _AVMClass
def test__AVMClass_make_object():
    avm_class = _AVMClass(name_idx=1, name='TestClass')

    obj1 = avm_class.make_object()
    obj2 = avm_class.make_object()

    assert isinstance(obj1, _AVMClass_Object)
    assert obj1.avm_class is avm_class
    assert obj2.avm_class is avm_class
    assert obj1 is not obj2
    assert repr(obj1) == 'TestClass#%x' % id(obj1)

# Generated at 2026-10-24 06:10:57.657402
# Unit test for method __repr__ of class _AVMClass
def test__AVMClass___repr__():
    avm_class = _AVMClass(1, 'TestClass')

    assert repr(avm_class) == '_AVMClass(TestClass)'

# Generated at 2026-10-24 06:11:00.162305
# Unit test for method __repr__ of class _AVMClass_Object

# Generated at 2026-10-24 06:11:02.685584
# Unit test for method __repr__ of class _AVMClass_Object

# Generated at 2026-10-24 06:11:05.099414
# Unit test for method __repr__ of class _AVMClass_Object

# Generated at 2026-10-24 06:11:07.514807
# Unit test for constructor of class _Multiname

# Generated at 2026-10-24 06:11:09.930879
# Unit test for constructor of class _Multiname

# Generated at 2026-10-24 06:11:12.348173
# Unit test for constructor of class _Multiname

# Generated at 2026-10-24 06:11:14.763018
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 06:11:17.177862
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 06:11:19.593848
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 06:11:22.490625
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-24 06:11:24.903038
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-24 06:11:27.319122
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-24 06:12:28.694557
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():import struct


# Generated at 2026-10-24 06:12:31.116971
# Unit test for method register_methods of class _AVMClass

# Generated at 2026-10-24 06:12:33.633618
# Unit test for method register_methods of class _AVMClass
def test__AVMClass_register_methods():
    avm_class = _AVMClass(7, 'TestClass')
    assert avm_class.method_names == {}
    assert avm_class.method_idxs == {}

    avm_class.register_methods({'foo': 1, 'bar': 2})
    assert avm_class.method_names == {'foo': 1, 'bar': 2}
    assert avm_class.method_idxs == {1: 'foo', 2: 'bar'}

    avm_class.register_methods({'baz': 3})
    assert avm_class.method_names == {'foo': 1, 'bar': 2, 'baz': 3}
    assert avm_class.method_idxs == {1: 'foo', 2: 'bar', 3: 'baz'}

# Generated at 2026-10-24 06:12:36.481891
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 06:12:52.457248
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)

# Generated at 2026-10-24 06:13:17.330329
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():from types import SimpleNamespace


# Generated at 2026-10-24 06:13:19.748422
# Unit test for method __hash__ of class _Undefined

# Generated at 2026-10-24 06:13:22.163510
# Unit test for method __hash__ of class _Undefined

# Generated at 2026-10-24 06:13:24.583149
# Unit test for method __hash__ of class _Undefined

# Generated at 2026-10-24 06:13:26.996615
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 06:13:29.410638
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 06:13:31.821020
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 06:13:34.237141
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-24 06:13:36.651363
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-24 06:13:39.064200
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-24 06:13:41.479917
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 06:13:43.892615
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 06:13:46.305487
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 06:13:48.719834
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 06:13:51.134224
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 06:13:53.769164
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 06:13:55.113058
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 06:13:57.847844
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 06:14:00.587089
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 06:14:08.589549
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 06:14:27.171968
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():interpreter = SWFInterpreter.__new__(SWFInterpreter)


# Generated at 2026-10-24 06:14:48.364228
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():interpreter = object.__new__(SWFInterpreter)

# Generated at 2026-10-24 06:14:50.783634
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 06:14:53.198761
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 06:15:28.505507
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 06:15:40.681184
# Unit test for method __repr__ of class _Undefined

# Generated at 2026-10-24 06:15:45.141089
# Unit test for method __repr__ of class _Undefined
def test__Undefined___repr__():value = _Undefined()

# Generated at 2026-10-24 06:15:47.652131
# Unit test for method __hash__ of class _Undefined

# Generated at 2026-10-24 06:15:50.068784
# Unit test for method __hash__ of class _Undefined

# Generated at 2026-10-24 06:15:52.489688
# Unit test for method __hash__ of class _Undefined

# Generated at 2026-10-24 06:15:55.079483
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 06:15:57.498683
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 06:15:59.913865
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2026-10-24 06:17:01.061940
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 06:17:04.059101
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 06:17:06.999561
# Unit test for constructor of class SWFInterpreter

# Generated at 2026-10-24 06:17:26.061706
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    # Arrange: create an interpreter containing known class metadata.

    # Act: extract the class.
    extracted = interpreter.extract_class('ExampleClass')

    # Assert:
    # 1. The correct _AVMClass is returned.
    # 2. Its methods/properties are populated.
    # 3. Its class initializer is called when requested.
    # 4. A second call returns the cached class.
    # 5. An unknown class raises the expected exception.

# Generated at 2026-10-24 06:17:29.141324
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 06:18:44.500368
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2026-10-24 06:19:01.192948
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():interpreter = object.__new__(SWFInterpreter)


# Generated at 2026-10-24 06:19:23.108825
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    # Bypass __init__, which requires and parses a complete SWF file.
    interpreter = SWFInterpreter.__new__(SWFInterpreter)

    avm_class = Mock()
    avm_class.cinit_idx = 42
    interpreter._classes_by_name = {
        'example.TestClass': avm_class,
    }

    class_initializer = Mock()
    interpreter.extract_function = Mock(return_value=class_initializer)

    result = interpreter.extract_class('example.TestClass')

    assert result is avm_class
    interpreter.extract_function.assert_called_once_with(avm_class, 42)
    class_initializer.assert_called_once_with([])
    assert avm_class.cinit_idx is None

    # The class initializer must only be executed once.
    second_result = interpreter.extract_class('example.TestClass')

    assert second_result is avm_class
    interpreter.extract_function.assert_called_once_with(avm_class, 42)
    class_initializer.assert_called_once_with([])

# Generated at 2026-10-24 06:19:32.628278
# Unit test for method __hash__ of class _Undefined
def test__Undefined___hash__():
    u = _Undefined()
    # returns int 0
    h = u.__hash__()
    assert h == 0
    assert isinstance(h, int)
    assert hash(u) == 0

    # consistent on repeated calls
    assert hash(u) == hash(u)

    # constant across instances
    assert hash(_Undefined()) == hash(_Undefined()) == 0

    # usable as dict key / in set (hashable despite falsy __bool__)
    d = {u: 'value'}
    assert d[u] == 'value'
    assert len({ _Undefined(), _Undefined() }) <= 2

# Generated at 2026-10-24 06:19:51.676354
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)


# Generated at 2026-10-24 06:20:34.993005
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():interpreter = SWFInterpreter.__new__(SWFInterpreter)


# Generated at 2026-10-24 06:20:53.115168
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():from types import SimpleNamespace

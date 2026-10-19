

# Generated at 2022-06-14 18:25:10.069513
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    import base64
    from io import BytesIO

    b = BytesIO(compat_b64decode(
        b'AlpGwA1E6wB077sGSsA==')) # ActionScript: test()
    swf = SWFInterpreter(b)
    swf._load_function(name='test', into=globals())

    open = swf.patch_function(name='open', into=globals())
    open(__file__) # target: type(f) == file
    open(FileNotFoundError()) # target: type(f) == IOError
    open(1, 2) # target: type(f) == IOError
    open('/') # target: type(f) == file
    open('/', 'r') # target: type(f) == file
   

# Generated at 2022-06-14 18:25:15.350905
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf = _get_test_swf()
    interpreter = SWFInterpreter(swf)
    avm_class = interpreter.extract_class(swf.script)
    for attr in avm_class.method_names:
        getattr(avm_class, attr)
    assert avm_class.method_pyfunctions['doit']([1, 1]) == 2

test_SWFInterpreter_extract_class()

# Generated at 2022-06-14 18:25:23.087941
# Unit test for method register_methods of class _AVMClass
def test__AVMClass_register_methods():
    class_ = _AVMClass(
        name_idx=0,
        name='_AVMClass',
        static_properties={
            b'$clinit': _AVMMethod(class_=class_, code=[])},
    )
    class_.register_methods({
        b'method1': 1, b'method2': 2, b'method3': 3})
    assert class_.method_names == {
        b'method1': 1, b'method2': 2, b'method3': 3}
    assert class_.method_idxs == {
        1: b'method1', 2: b'method2', 3: b'method3'}



# Generated at 2022-06-14 18:25:27.598438
# Unit test for method register_methods of class _AVMClass
def test__AVMClass_register_methods():
    avm_class = _AVMClass('avm_class0', 'avm_class0')
    methods = {'method0': 0, 'method1': 1}
    avm_class.register_methods(methods)
    assert avm_class.method_names == methods
    assert avm_class.method_idxs == methods



# Generated at 2022-06-14 18:25:39.221626
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = SWFInterpreter(SWFReader(open(os.path.join('tests', 'test.swf')), 0))

# Generated at 2022-06-14 18:25:44.372103
# Unit test for method register_methods of class _AVMClass
def test__AVMClass_register_methods():
    t = _AVMClass('FooClass', 'FooClass', {})
    t.register_methods({'init_1': 1, 'do_stuff_2': 2})
    assert t.method_idxs == {1: 'init_1', 2: 'do_stuff_2'}
    assert t.method_names == {'init_1': 1, 'do_stuff_2': 2}



# Generated at 2022-06-14 18:25:54.766599
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():

    def get_interpreter(pyfunc):
        class MyAVMClass(object):
            def __init__(self):
                self.variables = {}
                self.method_names = None
                self.method_pyfunctions = {}
                self.static_properties = {}
            def make_object(self):
                return self

        interpreter = SWFInterpreter()
        avm_class = MyAVMClass()
        interpreter.extract_function(avm_class, 'test')

        return interpreter

    def test_function():
        interpreter = get_interpreter(test_function)
        myobj = interpreter.global_scope['MyAVMClass'].make_object()
        return myobj.test()


# Generated at 2022-06-14 18:25:59.232548
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf = open(os.path.join(os.path.dirname(__file__), 'flash.swf'), 'rb').read()
    interp = SWFInterpreter(swf)
    interp.extract_class('Main')
    interp.extract_class('TopLevel')
    interp.extract_class('Array')


# Generated at 2022-06-14 18:26:06.797982
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interpreter = SWFInterpreter()
    avm_class = _AVMClass()
    avm_class.constant_strings = ['String']
    avm_class.static_properties = {'String': StringClass}
    avm_class.multinames = [
        _Multiname({
            'name': 'String',
            'kind': 11
        })
    ]
    avm_class.methods = {
        'String': [
            [42, 74, 93, 74, 71],
            [44, 0]
        ]
    }
    interpreter.extract_function(avm_class, 'String')
    assert avm_class.method_pyfunctions['String'](1) == '1'

# Generated at 2022-06-14 18:26:16.101064
# Unit test for method register_methods of class _AVMClass
def test__AVMClass_register_methods():
    from .utils import compile_method
    c = _AVMClass(0, b'test')
    c.register_methods({
        b'foo': 0,
        b'bar': 1,
        b'baz': 2,
        })
    c.methods[0] = compile_method(b'foo', b'', b'')
    c.methods[1] = compile_method(b'bar', b'', b'')
    c.methods[2] = compile_method(b'baz', b'', b'')
    assert c.method_names == { b'foo': 0, b'bar': 1, b'baz': 2 }
    assert c.method_idxs == { 0: b'foo', 1: b'bar', 2: b'baz' }
# Test for class Scope

# Generated at 2022-06-14 18:27:25.995914
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    import os
    filename = os.path.join(os.path.dirname(__file__), 'flashvars.txt')
    with open(filename, 'rb') as fileobj:
        content = fileobj.read()
    swf = SWFInterpreter(content)
    assert isinstance(swf.constant_pool, dict)
    for k, v in swf.constant_pool.items():
        assert isinstance(k, int)
        assert isinstance(v, compat_str)
    assert isinstance(swf.multinames, list)
    assert len(swf.multinames) == 24
    for name in swf.multinames:
        assert isinstance(name, _Multiname)
    assert isinstance(swf.methods, dict)

# Generated at 2022-06-14 18:27:33.753563
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from .swfinterpreter import SWFInterpreter  # Avoid circular import

    class Obj(object):
        def func(self, args):
            pass

    func = Obj().func
    res = SWFInterpreter.patch_function(func, '', 0, None)
    assert res() is None
    res = SWFInterpreter.patch_function(func, '', 1, None)
    assert res(4) is None
    res = SWFInterpreter.patch_function(func, '', 2, None)
    assert res(1, 2) is None
    res = SWFInterpreter.patch_function(func, '', 3, None)
    assert res(1, 2, 3) is None
    res = SWFInterpreter.patch_function(func, '', 4, None)
    assert res

# Generated at 2022-06-14 18:27:42.979927
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from .as3types import AS3Interpreter


# Generated at 2022-06-14 18:27:51.303679
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    filename = resource_filename(
        __name__, '../../test/big_buck_bunny_trailer_400.swf')
    with open(filename, 'rb') as f:
        swf = SWF(f)
    swf.parse_all_tags()
    interpreter = swf.swf_interpreter
    interpreter.extract_class('BigBuckBunny_Trailer_400')
    interpreter.extract_class('BigBuckBunny_Trailer_400_Trimmed')


# Generated at 2022-06-14 18:27:54.527848
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interpreter = SWFInterpreter()
    assert interpreter.extract_function(StringClass, 'String') is not None
    assert interpreter.extract_function(StringClass, 'reverse') is None


# Generated at 2022-06-14 18:28:07.494295
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    # load test SWF for this doctest
    interp = SWFInterpreter(
        open(test_path('test_swfinterpreter_extract_function.swf'), 'rb'))

    # check extracted function

# Generated at 2022-06-14 18:28:10.052633
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    interp = SWFInterpreter()
    assert interp.patch_function(None, None) is None
test_SWFInterpreter_patch_function()



# Generated at 2022-06-14 18:28:19.820837
# Unit test for constructor of class SWFInterpreter

# Generated at 2022-06-14 18:28:28.332418
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    mp4_filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'youtube-dl-master', 'tests', 'test-sample-42.swf')
    with open(mp4_filename, 'rb') as f:
        swf = f.read()
    swf_info = SWFInfo(swf)
    swf_interpreter = swf_info.interpreter

    # Create a synthesized AVM class
    avm_class = _AVMClass()
    avm_class.static_properties['String'] = StringClass
    avm_class.method_names.add('foo')
    avm_class.methods = [
        [(0, 0)]
    ]

# Generated at 2022-06-14 18:28:32.654792
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2022-06-14 18:29:44.553543
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:29:47.925578
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    # Testing for exception when variable class_index is not in
    # variable constant_pool_class
    with pytest.raises(KeyError) as exception_info:
        def_interpreter().extract_class(0)
    assert str(exception_info.value) == '0'

# Generated at 2022-06-14 18:29:51.250844
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    swfi = SWFInterpreter()
    swfi.patch_function('TestClass$testMethod', lambda x: x + 2)
    assert swfi.method_pyfunctions['TestClass$testMethod'](1) == 3

# Generated at 2022-06-14 18:29:56.450312
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from .amf import SWFClass
    interpreter = SWFInterpreter()

    class TestClass(object):
        pass
    test_class = TestClass()
    avm_class = SWFClass(interpreter, name='TestClass')
    interpreter.extract_method(avm_class, 'TestMethod', test_class)

    assert avm_class.method_pyfunctions == {'TestMethod': test_class}


# Generated at 2022-06-14 18:30:07.777294
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from .swf_parse import read_swf, TagCodes

    # SWF from http://www.action-script.org/forums/showthread.php3?t=191020
    # with the exception of first 4 bytes

# Generated at 2022-06-14 18:30:12.428187
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    swf = open(os.path.join(
        os.path.dirname(__file__), '..', 'test', 'test.swf'), 'rb').read()
    int = SWFInterpreter(swf)

    assert len(int.avm_classes) == 1
    avm_class = int.avm_classes[0]
    assert avm_class.qname_str == 'test.Main'
    assert len(avm_class.method_pyfunctions) == 0

    int.patch_function(avm_class, 'Main')

    assert len(int.avm_classes) == 1
    avm_class = int.avm_classes[0]
    assert avm_class.qname_str == 'test.Main'

# Generated at 2022-06-14 18:30:15.827391
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    def foo(x):
        foo_helper()

    interpreter = SWFInterpreter()
    interpreter.patch_function(foo)

    with pytest.raises(AttributeError):
        foo_helper()


# Generated at 2022-06-14 18:30:26.435635
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    # This test is for finding a bug in the method of
    # SWFInterpreter object, SWFInterpreter.parse_method()
    # which causes the whole interpreter to crash.
    interpreter = SWFInterpreter()
    interpreter.extract_method(
        'RtmpSampleAccess',
        0,
        bytearray(base64.b64decode(b'AQEABIYABAADBAIAAAAMAgAAAAAAAIADAACAAgAAAAAgA'
                                   b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
                                   b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'))
    )



# Generated at 2022-06-14 18:30:36.403134
# Unit test for constructor of class SWFInterpreter

# Generated at 2022-06-14 18:30:48.271133
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    class_parser = ClassParser()

# Generated at 2022-06-14 18:32:28.289247
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    avm = SWFInterpreter()
    def func():
        pass
    assert avm.extract_function(func) is func



# Generated at 2022-06-14 18:32:38.234969
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():

    swf_interp = SWFInterpreter()
    swf_interp.version = 12

    # Define class TestClass
    class_id = 0
    class_name = 'TestClass'
    class_super_id = 0
    class_protected_ns = 0
    class_interfaces = []
    class_protected_ns_id = 0
    class_init = 0

    swf_interp.multinames += [
        _Multiname(
            kind=3,
            ns=0,
            name=class_name
        ),
    ]


# Generated at 2022-06-14 18:32:48.674332
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from io import BytesIO
    from .bitstream import BitStream
    from .swfdecompiler import SWFDecompiler
    from .avmgenerator import AVMGenerator
    from .swfobject import SWFObject

    def hexread(bs, count):
        return ' '.join('%02x' % ord(b) for b in bs.readBytes(count))

    swf = SWFObject()

    # AVM2, should be decompiled

# Generated at 2022-06-14 18:32:59.176540
# Unit test for constructor of class SWFInterpreter

# Generated at 2022-06-14 18:33:09.515171
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    interp = SWFInterpreter()
    interp.constant_names = ['Object', 'TextField', 'TextFormat', 'String']
    interp.constant_strings = ['Object', 'TextField', 'TextFormat', 'String']

# Generated at 2022-06-14 18:33:15.105949
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from . import swfdecompiler
    swf = swfdecompiler.SWF('fixtures/adobetv.swf')
    swf.decompile_all()
    interpreter = SWFInterpreter(swf.abc_models)
    interpreter.extract_function(swf.avm_classes[0], 'decrypt')


# Generated at 2022-06-14 18:33:26.989315
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    assert_raises(IOError, SWFInterpreter, 'non-existent-file')
    assert_raises(ValueError, SWFInterpreter,
                  os.path.join(os.path.dirname(__file__), 'helloworld.swf'))
    f = open(
        os.path.join(os.path.dirname(__file__), 'helloworld.swf'), 'rb')
    swf = SWFInterpreter(f)
    assert swf.version == 8
    assert swf.file_length == 161
    assert swf.frame_size == Rectangle(0, 0, 160, 160)
    assert swf.frame_rate == 1
    assert swf.frame_count == 1


# Generated at 2022-06-14 18:33:31.121944
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    interp = SWFInterpreter()
    interp.extract_class(ClassName='String')
    interp.extract_class(ClassName='Array')
    interp.extract_class(ClassName='Object')

# Generated at 2022-06-14 18:33:38.910879
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():

    coder = io.BytesIO(b'\x09\x03\x01\x00\x05\x00\x01\x01\x02')

    class SwfTestInterpreter(SWFInterpreter):
        _read_byte = staticmethod(lambda *args: b'\0')

    swf = SwfTestInterpreter()
    swf.extract_function('foo', 'bar', coder)

# }}} unit test for SWFInterpreter

# Generated at 2022-06-14 18:33:43.016495
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf = SWFInterpreter(os.path.join(
        get_testdata_dir(), 'test.swf'))
    swf.parse()
    swf.extract_class('Player')
    assert isinstance(swf.classes['Player'], _AVMClass)
    assert isinstance(swf.classes['Player'].make_object(), _AVMClass_Object)



# Generated at 2022-06-14 18:25:12.262237
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf = open(os.path.join(
        os.path.split(__file__)[0], 'crc32_swfs', 'level2_9951.swf'), 'rb').read()
    interp = SWFInterpreter(swf)
    crc32_level2 = interp.classes['org.flowplayer.pseudostreaming.Level2Crc32']
    assert isinstance(crc32_level2, _AVMClass)
    func = crc32_level2.static_properties['crc32']
    assert isinstance(func, _AVMFunction)
    assert func.args == ['bytes']
    assert func.code.find('this.table =') != -1


# Generated at 2022-06-14 18:25:22.260561
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swfi = SWFInterpreter(data=b'\x46\x57\x53\x01\x01\x00\x00\x00\x07\x00\x04\x01\x00\x00\x00\x01\x00\x00\x00\x01\x02\x00\x10\x00\x00\x00\x02\x00\x01\x00\x03\x00\x00\x00\x00\x00')
    swfi.extract()
    cls1 = swfi.classes[0]
    cls2 = swfi.classes[1]
    assert cls1.name == 'MainTimeline', cls1.name
    assert cls2.name == '', cls2.name

# Generated at 2022-06-14 18:25:32.939896
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from .flash_proxy import FlashProxy
    import os
    os.chdir(os.path.dirname(__file__))
    with open('../../test/test.swf', 'rb') as f:
        swf = f.read()
    interpreter = SWFInterpreter(swf)
    assert len(interpreter.avm2_scripts) > 0
    interpreter.avm2_scripts[0].avm_class.make_object()
    # Call a method of that object
    FlashProxy(
        'SWFInterpreterTest', 'Test',
        lambda x, y: x + y)('a', 'b') == 'ab'

# Test for method get_avm_classes() of class SWFInterpreter

# Generated at 2022-06-14 18:25:42.886036
# Unit test for constructor of class SWFInterpreter

# Generated at 2022-06-14 18:25:51.105442
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    swf = SWFInterpreter(b'')
    pos = 0
    b = io.BytesIO()

    # i_popscope
    b.write(_write_byte(1))
    # i_pushbyte
    b.write(_write_byte(36))
    b.write(_write_byte(0x00))
    # i_returnvoid
    b.write(_write_byte(71))
    swf.patch_function('f', b.getvalue())



# Generated at 2022-06-14 18:25:59.049668
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from ts_log import log

    log('Initializing interpreter')
    interp = _SWFInterpreter()
    f = compat_urlopen(test_url)
    log('Parsing swf')
    swf = SWF(f)
    assert isinstance(swf, SWF)

    log('Exporting')
    interp.parse_exports(swf)

    log('Extracting classes')
    for name, c in interp.classes.items():
        assert isinstance(c, _AVMClass)
        c.make_class()

    log('Creating main')
    main = interp.classes.get('', None)
    assert main is not None
    assert isinstance(main, _AVMClass)

    log('Creating main object')
    main_obj = main.make_object()
   

# Generated at 2022-06-14 18:26:01.452328
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = SWFInterpreter()
    swf.read_file(get_testpath('media/find_video_info.swf'))

if __name__ == '__main__':
    test_SWFInterpreter()

# Generated at 2022-06-14 18:26:05.522676
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interp = SWFInterpreter()
    test_class = _AVMClass('TestClass', interp)
    test_class.static_properties['play_list'] = {'title': '', 'type': 'video'}
    interp.extract_function(
        test_class, 'play_list')



# Generated at 2022-06-14 18:26:15.155265
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    with open('lib/io.swf', 'rb') as f:
        swf = SWF(f)
        interpreter = SWFInterpreter(swf)

    root_class = interpreter.avm_classes[0]
    str_class = interpreter.avm_classes[1]

    # Variable declarations
    assert root_class.variables[''] == []
    assert root_class.variables['decodeURI'] == (
        root_class.static_properties['decodeURI'])
    assert root_class.variables['__constructor__'] == root_class.make_object()
    assert len(root_class.variables) == 5

    # Class and method declarations
    assert isinstance(root_class.static_properties['String'], _AVMClass)

# Generated at 2022-06-14 18:26:22.774990
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interpreter = SWFInterpreter(b'')
    interpreter.constant_strings = ['abc', 'def', 'ghi']
    interpreter.register_class('abc', ['def', 'ghi'],
        {})
    avm_class = interpreter.classes['abc']
    avm_class.method_names = ['def']
    avm_class.variables = {
        'def': 1,
        'ghi': 2,
    }
    try:
        interpreter.extract_function(
            avm_class, 'def')
        assert False
    except NotImplementedError:
        assert True



# Generated at 2022-06-14 18:27:11.172205
# Unit test for method register_methods of class _AVMClass
def test__AVMClass_register_methods():
    x = _AVMClass('x', 'x')
    x.register_methods({'a': 1, 'b': 2})
    x.method_names == {'a': 1, 'b': 2}
    x.method_idxs == {1: 'a', 2: 'b'}



# Generated at 2022-06-14 18:27:13.600735
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    swfi = SWFInterpreter()
    swfi.patch_function(None, None, None) # FIXME: not implemented

# Generated at 2022-06-14 18:27:23.943916
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    # Simple value
    instantiate_and_test(1234, 'Function0', [])
    # Undefined
    instantiate_and_test(undefined, 'Function1', [])
    # Null
    instantiate_and_test(None, 'Function2', [])
    # True
    instantiate_and_test(True, 'Function3', [])
    # False
    instantiate_and_test(False, 'Function4', [])
    # Constant double
    instantiate_and_test(12.34, 'Function5', [])
    # Constant string
    instantiate_and_test('hello', 'Function6', [])
    # Registers
    instantiate_and_test('hello', 'Function7', ['world'])
    # Register usage

# Generated at 2022-06-14 18:27:28.997654
# Unit test for method register_methods of class _AVMClass
def test__AVMClass_register_methods():
    cls = _AVMClass(None, None)
    cls.register_methods({'foo': 0x1234, 'bar': 0x9abc})
    assert cls.method_names == {'foo': 0x1234, 'bar': 0x9abc}
    assert cls.method_idxs == {0x1234: 'foo', 0x9abc: 'bar'}



# Generated at 2022-06-14 18:27:34.488297
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    si = SWFInterpreter(None, [], [])
    class AVMClass:
        flags = 0
        variables = {}
        static_properties = {}
        method_codes = {}
        method_names = set()
    cls = AVMClass()
    si.extract_function(cls, 'AMethod')


# Generated at 2022-06-14 18:27:43.450519
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:27:51.671218
# Unit test for method register_methods of class _AVMClass
def test__AVMClass_register_methods():
    assert '_AVMClass.register_methods' in globals(), 'Method' + ' _AVMClass.register_methods not in globals'
    #
    # _AVMClass('name', 'methods')
    #
    avm_class = _AVMClass(0, 0)
    avm_class.register_methods({'test': 42})

    assert avm_class.method_names == {'test': 42}
    assert avm_class.method_idxs == {42: 'test'}



# Generated at 2022-06-14 18:27:58.931006
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    # Test AVMClass
    assert isinstance(StringClass, _AVMClass)

    # Test AVMClass methods
    assert isinstance(StringClass.static_properties['String'], _AVMClass)
    assert isinstance(StringClass['prototype'], _AVMClass_Object)
    assert isinstance(StringClass['prototype']['fromCharCode'],
                      _AVMClass_Object)

    # Test AVMClass.make_object()
    assert isinstance(StringClass.make_object(), _AVMClass_Object)

    # Test _AVMClass_Object
    assert isinstance(StringClass['prototype'], _AVMClass_Object)

    # Test _AVMClass_Object methods
    assert isinstance(
        StringClass['prototype']['charCodeAt'], _AVMClass_Object)

    # Test _

# Generated at 2022-06-14 18:28:09.604084
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    f = io.BytesIO()
    f.write(b'FWS')
    # Version
    f.write(b'\x08')
    # File length
    f.write(b'\x00\x00\x00\x00')

    # Rect
    f.write(b'\x00\xc4\x01')
    # Frame rate
    f.write(b'\x00\x01\x00\x00')
    # Frame count
    f.write(b'\x00\x01')
    # Tag 1: DoABC
    f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00')
    # Tag 1: DoABC

# Generated at 2022-06-14 18:28:15.667433
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = SWFInterpreter()
    assert swf.constant_strings == []
    assert swf.methods == []
    assert swf.multinames == []
    assert swf.traits == []
    assert swf.plain_traits == []
    assert isinstance(swf.classes, dict)

    assert swf.get_method_pyfunction(None, None) is None


# Generated at 2022-06-14 18:29:06.166928
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = SWFInterpreter(open(os.path.join(os.path.dirname(__file__),
                                           'flash0.swf'), 'rb'))


# Generated at 2022-06-14 18:29:18.055939
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    interpreter = SWFInterpreter()
    interpreter.swf = SWF()
    interpreter.swf.constant_pool.strings = [
        'indexOf',
        'slice']
    interpreter.multinames = [
        None,
        _MultinameL('indexOf'),
        _MultinameLA('indexOf', 0),
        _MultinameLA('slice', 1),
    ]

    avm_class = _AVMClass()
    func = avm_class.add_method(
        'test', [_MethodParam('param1', None)])

# Generated at 2022-06-14 18:29:28.746146
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:29:32.274443
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from .swfdecompiler import decompile_swf
    test_swf = decompile_swf('tests/swf/textfield.swf')
    swfi = SWFInterpreter(test_swf)
    cls = swfi.extract_class(test_swf, '_level0')
    assert cls.name == '_level0'
    expected_functions = set([
        '_level0',
        '_level0_init',
    ])
    assert set(cls.method_names) == expected_functions
    assert callable(cls.make_object())

# Generated at 2022-06-14 18:29:40.456847
# Unit test for method extract_class of class SWFInterpreter

# Generated at 2022-06-14 18:29:48.691595
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    import unittest
    from .test_zlib import Inflated
    from .test_amf0 import AMF0TestCase

    class InflatedSWF(Inflated):
        def __init__(self, infl_data):
            super(InflatedSWF, self).__init__(infl_data)
            self.raw_data = None

    class SWFInterpreterTestCase(AMF0TestCase):
        TEST_FILES = ['test.swf']

        def test_swf(self):
            for file_path in self.TEST_FILES:
                test_file = InflatedSWF(
                    compat_urlopen(
                        'http://rg3.github.io/youtube-dl/test/' + file_path,
                        timeout=10
                    ).read()
                )

# Generated at 2022-06-14 18:29:51.333278
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from .swf_interpreter_test import test_SWFInterpreter_patch_function
    test_SWFInterpreter_patch_function(GLOBAL_INTERPRETER)



# Generated at 2022-06-14 18:30:00.106114
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from .swf import SWF
    from .tags.doabc import DoABC
    from .tags.avm2 import DoAction, DoInitAction
    from .abc import detect_abc_version

    class MockSWF(object):
        def get_doabc_tags(self):
            return [
                DoABC(swf=self, flags=1, name=u'ABC1',
                      data=b'\x00\x11\x07test\x05test\x00\x00\x00\x00\x00'),
                DoABC(swf=self, flags=1, name=u'ABC2',
                      data=b'\x00\x11\x07test\x05test\x00\x00\x00\x00\x00'),
            ]

    swf = MockSWF()
   

# Generated at 2022-06-14 18:30:01.992411
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    assert '@classmethod' not in inspect.getsource(SWFInterpreter.patch_function)


# Generated at 2022-06-14 18:30:06.677649
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    interpreter = SWFInterpreter()
    assert interpreter.constant_strings == []
    assert interpreter.constant_namespaces == []
    assert interpreter.constant_namespace_sets == []
    assert interpreter.constant_multinames == []
    assert interpreter.classes_by_name == {}
    assert interpreter.classes == []
    assert interpreter.multinames == []
    assert interpreter.method_body_infos == []


# Generated at 2022-06-14 18:31:40.294865
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    def _swf_class_to_code(avm_class):
        return '\n'.join(
            '%s = %r'
            % (key, avm_class.static_properties[key])
            for key in avm_class.static_properties)


# Generated at 2022-06-14 18:31:50.907830
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    _SWFInterpreter = SWFInterpreter
    class SWFInterpreter(_SWFInterpreter):
        def extract_function(self, avm_class, name):
            assert name == 'test'
            return lambda x: x + 1
    swf = SWFInterpreter(b'\x00')
    swf.constant_strings = ['test']
    swf.multinames = [_Multiname('test')]
    avm_class = _AVMClass('test')
    avm_class.method_names = ['test']
    swf.avm_classes = {
        'test': avm_class
    }
    swf.patch_function(avm_class, 'test')

# Generated at 2022-06-14 18:32:01.662867
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    class AVMClass__2(object):
        static_properties = {
            "Clicks": "Clicks",
            "ClickTag": "ClickTag",
            "ClickTag2": "ClickTag2",
        }
        method_names = set(['CallFrame'])
        method_pyfunctions = {}
        class_name = 'Data'
        variables = {}

    class AVMClass__1(object):
        static_properties = {
            'FSCommand': 'FSCommand',
            'adURL': 'adURL',
            'bgcolor': 'bgcolor',
        }

# Generated at 2022-06-14 18:32:09.713092
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    import os
    from .swfdecompiler import AVM2Decompiler
    from .parser import SWFParser
    import zlib
    path = os.path.join(os.path.dirname(__file__), 'testfiles', 'test.swf')
    with open(path, 'rb') as inf:
        swf = inf.read()
    swf = zlib.decompress(swf)
    parser = SWFParser(swf)
    parser.parse_swf_file()
    swfdecompiler = AVM2Decompiler(parser.avm2)
    swfdecompiler.decompile()

    cls = swfdecompiler.get_class('com.netease.recorder.netease.common.VideoFormat')

# Generated at 2022-06-14 18:32:18.286344
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    import zipfile

    with zipfile.ZipFile("test.swf", "r") as zf:
        with zf.open("test.xml", "r") as f:
            info = f.read()
            assert info == b'<test />'
        with zf.open("test.py", "r") as f:
            code = f.read()
            assert code == b'\tprint("Hello, world!")\n'

    swf = SWFInterpreter(zf)
    assert swf.extract_function(swf.scripts[0], 'main')([]) == 'Hello, world!'

# Extract functions with SWFInterpreter
swf = SWFInterpreter(sys.argv[1])

# Generated at 2022-06-14 18:32:20.864585
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    si = SWFInterpreter()
    si.patch_function(None, None, None)

# Generated at 2022-06-14 18:32:27.376165
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from io import BytesIO

    f = BytesIO(open(
        os.path.join(os.path.dirname(__file__),
                     'flash', 'test_all.swf'), 'rb').read())
    swf = SWFInterpreter(f)
    assert swf.coder.read(3) == b'CWS'

    # TODO: test read_byte()
    # TODO: test u30()
    # TODO: test s24()
    # TODO: test parse_tables()
    # TODO: test parse_method_body()
    # TODO: test parse_script_body()
    # TODO: test parse_method_info()
    # TODO: test parse_class_info()
    swf.parse_abc(swf.abc_data)
   

# Generated at 2022-06-14 18:32:37.413444
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    class DICT(dict):
        pass

    class DICT2(dict):
        pass

    class DICT3(dict):
        pass

    class DICT4(dict):
        pass

    class DICT5(dict):
        pass

    class DICT6(dict):
        pass

    class DICT7(dict):
        pass

    class DICT8(dict):
        pass

    class DICT9(dict):
        pass

    class DICT0(dict):
        pass

    class DICT1(dict):
        pass

    class DICT2(dict):
        pass

    class DICT3(dict):
        pass

    class DICT4(dict):
        pass

    class DICT5(dict):
        pass

    class DICT6(dict):
        pass


# Generated at 2022-06-14 18:32:48.301609
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    def check_patched(pyfunc, sample_args, expected_res):
        assert pyfunc(sample_args) == expected_res, 'pyfunc(%r) != %r' % (
            sample_args, expected_res)
    si = SWFInterpreter()
    for opcode in range(256):
        if opcode == 118:  # convert_d
            continue
        if opcode == 119:  # convert_b
            continue
        if opcode == 120:  # convert_o
            continue
        if opcode == 121:  # convert_u
            continue
        if opcode == 122:  # convert_i
            continue

# Generated at 2022-06-14 18:32:55.585083
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    # Test for method extract_function( (SWFInterpreter) )
    interp = SWFInterpreter(None)
    interp.extract_function(1, 1)
    interp.extract_function(2, 1)
    interp.extract_function(3, 2)
    interp.extract_function(4, 2)
# end of test for method extract_function
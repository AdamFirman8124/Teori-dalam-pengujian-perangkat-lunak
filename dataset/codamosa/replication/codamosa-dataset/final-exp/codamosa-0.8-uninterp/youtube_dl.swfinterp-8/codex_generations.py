

# Generated at 2022-06-14 18:25:26.835481
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    with open(os.path.join(os.path.dirname(os.path.realpath(
            __file__)), '..', 'tests', 'static', 'yswf-base.swf')) as f:
        swf = f.read()
    interp = SWFInterpreter(swf)

    # Test constant pool

# Generated at 2022-06-14 18:25:34.354655
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    swf_interpreter = SWFInterpreter(b'')
    assert swf_interpreter.extract_function is SWFInterpreter.extract_function

    class MyInterpreter(SWFInterpreter):
        pass
    MyInterpreter.extract_function = lambda self, *args, **kwargs: 'foo'
    assert MyInterpreter(b'').extract_function('foo') == 'foo'
test_SWFInterpreter_extract_function()


# Generated at 2022-06-14 18:25:35.718740
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    pass


# Generated at 2022-06-14 18:25:47.264277
# Unit test for method register_methods of class _AVMClass
def test__AVMClass_register_methods():
    from .swfdecompressor import (
        _AVMClass_Object,
        _ScopeDict,
        _AVMClass,
    )
    assert isinstance(
        _AVMClass_Object, type), 'is instance returned incorrect type'
    assert isinstance(
        _ScopeDict, type), 'is instance returned incorrect type'
    assert isinstance(
        _AVMClass, type), 'is instance returned incorrect type'
    ac = _AVMClass('a', 'b', {'1': 2})
    assert isinstance(
        ac, _AVMClass), 'is instance returned incorrect type'
    ac = _AVMClass('a', 'b')
    assert ac.name_idx == 'a', 'attribute name_idx of class _AVMClass has incorrect value'

# Generated at 2022-06-14 18:25:56.616351
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:26:01.389288
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from io import BytesIO
    from .swftags import TagDefineBinaryData

    coder = BytesIO()
    coder.write(b'\x11ABCDEFG')
    tag = TagDefineBinaryData(0, 0, coder)
    interpreter = SWFInterpreter()
    interpreter.read_tags([tag])
    assert interpreter.binary_data == {
        0: b'\x11ABCDEFG',
    }
    assert interpreter.classes == {}



# Generated at 2022-06-14 18:26:12.068631
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from io import BytesIO
    from .flash_audio import _audiodecoders
    from .common import parse_swf_version, CONTROL_TAG_CLIP_ACTIONS
    from .swfdata import SWFData
    swf = SWFData()
    swf.version = parse_swf_version('9')


# Generated at 2022-06-14 18:26:23.629377
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    # Create an instance of _SWFInterpreter_extract_class in order to
    # test foo
    class_extractor = _SWFInterpreter_extract_class()

    # Define some variables
    ctx = None


    avm_class = pyamf.util.BufferedByteStream()
    avm_class.write('\x0a\x01\x00\x64\x01\x00\x00')
    avm_class.seek(0)

    def s8():
        return struct.unpack('>b', avm_class.read(1))[0]

    def u30():
        i = 0
        val = 0
        while True:
            c = s8()
            val |= (c & 0x7f) << (7 * i)

# Generated at 2022-06-14 18:26:35.187268
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf_file = os.path.join(os.path.dirname(__file__),
                            'flashplayer-11.9.900.117.swf')
    swf = open(swf_file, 'rb').read()
    player = SWFInterpreter(swf)


# Generated at 2022-06-14 18:26:46.563262
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    global _builtin_classes

    def assert_class_dict(avm_class):
        assert avm_class.variables == {
            'staticValue1': 1,
            'staticValue2': 2,
            'staticValue3': 3,
            'staticValue4': 4,
            'staticValue5': 5}
        assert avm_class.method_names == {
            'Test1', 'Test2', 'Test3', 'Test4', 'Test5'}
        assert avm_class.class_name == "TestClass"

    for fn in sorted(glob.glob('../swfinterpreter/test_files/class*.swf')):
        swf_file = io.BytesIO(open(fn, 'rb').read())

# Generated at 2022-06-14 18:27:39.258865
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    intp = SWFInterpreter()
    intp.extract_class('com.adobe.serialization.json.JSON')
    intp.extract_class('com.longtailvideo.jwplayer.utils.Strings')
    intp.extract_class('com.longtailvideo.jwplayer.utils.ParseUrl')
    intp.extract_class('com.longtailvideo.jwplayer.utils.Configger')
    intp.extract_class('com.longtailvideo.jwplayer.utils.NetClient')
    intp.extract_class('com.longtailvideo.jwplayer.utils.Network')
    intp.extract_class('com.longtailvideo.jwplayer.utils.Logger')

# Generated at 2022-06-14 18:27:42.754125
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    with _open_swf('swfdec_video_player.swf', 'rb') as swf:
        interp = SWFInterpreter(swf)
        cls = interp.extract_class(0)
        assert '__dict__' in cls.static_properties

# Generated at 2022-06-14 18:27:49.647665
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    # Silly test; method extract_function is only called for method 'initialize_AVM2'
    si = SWFInterpreter('tests/flashplayer11_2_202_233_ubuntu.bin', {})
    si.extract_function('AVM2', 'initialize_AVM2')
    
    
# Class for method find_flash_plugins of module utils

# Generated at 2022-06-14 18:27:52.092534
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():

    def _test():
        si = SWFInterpreter(None, {})
        si.extract_function(None, None)

    _run_and_catch_pytest(
        _test, NotImplementedError, 'not implemented yet')



# Generated at 2022-06-14 18:27:59.143517
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    class _FakeAVMClass(object):
        def __init__(self, method_names, static_properties, method_defaults):
            self.method_defaults = method_defaults
            self.static_properties = static_properties
            self.method_names = method_names
        def make_object(self):
            if 'avm_class' in self.__dict__:
                obj = _ScopeDict()
                obj.avm_class = self
                return obj
            else:
                return self
            # return _ScopeDict(self.method_defaults)
    method_names = {'foo': 0, 'bar': 1}
    static_properties = {'baz': 42}
    method_defaults = ['Bar', 'Foo']

# Generated at 2022-06-14 18:28:06.909096
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    _, video_id = video_id_re.search(
        'https://www.dailymotion.com/video/x65n5ut').groups()

    swf_interpreter = SWFInterpreter(
        compat_urllib_request.urlopen(
            'http://www.dailymotion.com/swf/video/%s'
            % video_id))
    video_class = swf_interpreter.extract_class('Video')
    assert isinstance(video_class, _AVMClass)


# Generated at 2022-06-14 18:28:09.746511
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    interpreter = SWFInterpreter()
    interpreter.extract_function(None, 'foo', patch_function=True)
test_SWFInterpreter_patch_function()


# Generated at 2022-06-14 18:28:10.769575
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    assert SWFInterpreter(b'')



# Generated at 2022-06-14 18:28:21.346827
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf_path = os.path.join(
        os.path.dirname(__file__),
        'flash', 'Connection.swf')
    with open(swf_path, 'rb') as f:
        swf = f.read()

    swf_interpreter = SWFInterpreter(swf)

# Generated at 2022-06-14 18:28:32.533527
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:29:35.299605
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    swf_interpreter = SWFInterpreter()
    swf_interpreter.patch_function('rtmpe://helper.twitch.tv/', 'onMetaData')
    assert swf_interpreter.functions['onMetaData'] == \
        RTMPPacket.onMetaData

# Generated at 2022-06-14 18:29:44.648871
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    class_text = """
        public function $23(param1, param2, param3) {
            var _loc1 = null;
            this.var1 = param1;
            this.var2 = param2;
            this.var3 = param3;
            return;
        }
    """
    class_text = re.sub(r'\s+', ' ', class_text)

    intp = SWFInterpreter()
    avm_class = intp.parse_class(class_text)
    assert avm_class.name == '$23'
    assert 'var1' in avm_class.variables
    assert 'var2' in avm_class.variables
    assert 'var3' in avm_class.variables
    assert '$23' in avm_class.method_pyfun

# Generated at 2022-06-14 18:29:48.719270
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    avm_class = _AVMClass('test', [], [])
    swf = SWFInterpreter(None, avm_class)

    def func(args):
        return 'hello'

    swf._patch_function(avm_class, 'test', func)

    assert avm_class.method_pyfunctions['test'] == func

# Generated at 2022-06-14 18:29:53.746761
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    # Callable test_SWFInterpreter_patch_function
    from io import BytesIO
    from .abc import ABCFile
    from .abc import ABCMethodBody
    from .abc import ABCMethodInfo
    from .abc import ABCException
    from .abc import ABCInstanceInfo
    from .abc import ABCMultiname
    from .abc import ABCTrait

    # Assign parameters passed from test runner

# Generated at 2022-06-14 18:30:02.178261
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from io import BytesIO
    from collections import namedtuple
    from time import time, sleep
    import pyamf
    import pyamf.util.pure

    pyamf.remoting.decode = pyamf.remoting.decode.copy_context()
    pyamf.AMF0.decode = pyamf.AMF0.decode.copy_context()
    pyamf.AMF3.decode = pyamf.AMF3.decode.copy_context()
    pyamf.util.pure.decode = pyamf.util.pure.decode.copy_context()

    def _decode(stream):
        return pyamf.remoting.decode(stream, context=pyamf.AMF3)


# Generated at 2022-06-14 18:30:10.091341
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from .test import test_data
    from .test.support_swf_interpreter import _SWFInterpreter_UnitTest
    from .utils import save_file
    from .swfdecompiler import SWFDecompiler

    for T in _SWFInterpreter_UnitTest:
        if T.data_key not in test_data:
            continue
        swfdata = test_data[T.data_key]
        swf = SWFDecompiler(swfdata)
        swf.extract_class(T.class_name)
        if not T.saved_class_file:
            continue
        save_file(T.saved_class_file, swf.as_string())

# Generated at 2022-06-14 18:30:16.153798
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from io import BytesIO

    # Constructor
    SWFInterpreter(BytesIO(), BytesIO(), {})

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    with open(filename, 'rb') as f:
        interpreter = SWFInterpreter(
            f, BytesIO(), {
                'trace': print,
            })
        interpreter.interpret()

# Generated at 2022-06-14 18:30:29.125290
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from io import BytesIO
    from .swfdecompiler import SWFDecompiler

    # A function defined in the middle of an ABC code
    f = BytesIO(SWFInterpreter._test_data_extract_function_code)

    abc_defs, _ = SWFDecompiler.read_abc_file(f)
    assert len(abc_defs) == 1

    custom_class = abc_defs[0]
    assert isinstance(custom_class, _AVMClass)

    assert len(custom_class.method_names) == 1
    assert 'myMethod' in custom_class.method_names
    assert 'myMethod' not in custom_class.method_pyfunctions

    # Create an interpreter
    interpreter = SWFInterpreter()

# Generated at 2022-06-14 18:30:38.868618
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    class SWFInterpreterMock(SWFInterpreter):
        def extract_pyfunction(self, avm_class, func_name, func_idx):
            func_name, func_idx = func_name, func_idx
            def resfunc(args):
                return args
            return resfunc

    interpreter = SWFInterpreterMock()

    avm_class = DictObj()
    avm_class.methods = {
        'a': 0,
        'b': 1,
        'c': 2,
    }
    avm_class.method_pyfunctions = {}

    res = interpreter.extract_function(avm_class, 'a')
    assert res([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert res is interpreter.extract

# Generated at 2022-06-14 18:30:50.375459
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    si = SWFInterpreter()
    swf = open(os.path.join(os.path.dirname(__file__), 'test.swf'), 'rb')
    si.parseSWF(swf)

    assert 'VideoPlayer' in si.classes
    vp = si.classes['VideoPlayer']
    assert vp.name == 'VideoPlayer'
    assert vp.base == 'Sprite'
    assert vp.traits == ['_vr', 'myVar', '_yj', '_yn', '_fj', '_fk', '_fu',
                          '_tx', '_sn', '_tk', '_ej', '_ye', '_xw', '_wx',
                          '_xm', '_fh']
    assert len(vp.method_names) == 3

# Generated at 2022-06-14 18:32:56.537820
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    swf_file = open('test/swf/sample.swf', 'rb')
    swf = swf_file.read()
    swf_file.close()
    swf_interp = SWFInterpreter(swf)

    avm_class = swf_interp.abc_data.classes[0]
    func_index = avm_class.instance_methods[0].index
    method_name = avm_class.instance_methods[0].name
    res_function = swf_interp.extract_function(avm_class, method_name)
    assert res_function(avm_class.make_object()) == 'res'

# Generated at 2022-06-14 18:33:05.016561
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    swf = SWFInterpreter(BytesIO.BytesIO(b''), None)

# Generated at 2022-06-14 18:33:12.476009
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    # Interpret a SWF binary to generate a function for test.
    with open(os.path.join(os.path.dirname(__file__), 'test', 'test.swf'), 'rb') as f:
        data = f.read()
    interpreter = SWFInterpreter(data)
    res = interpreter.run('test_func')
    assert res == (2, 3)

if __name__ == '__main__':
    test_SWFInterpreter()

# Generated at 2022-06-14 18:33:22.134531
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interpreter = SWFInterpreter()

# Generated at 2022-06-14 18:33:31.644719
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf_data = open(os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'test_video_extract_json_data.swf'), 'rb').read()
    swf = _SwfFile('test_video_extract_json_data.swf', swf_data)

    avm_class = swf.extract_class(
        tag_body=swf.tags[-1].body, class_name='PlayerConfig')
    assert avm_class.make_object().avm_class is avm_class
    player_config = avm_class.make_object()
    assert player_config.playerId == 'player_1_1j7i8pvz'
    assert player_config.author == 'WMG'
   

# Generated at 2022-06-14 18:33:41.678901
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():

    def test_one_function(class_name, method_name, expected_func):
        class_name = compat_str(class_name)
        method_name = compat_str(method_name)

        avm2_file = os.path.join(
            os.path.split(__file__)[0], 'avm2swf')
        swf = SWFInterpreter(open(avm2_file, 'rb'), 'FLV')

        avm_class = swf.avm_classes[class_name]
        extracted_function = swf.extract_function(avm_class, method_name)

        assert extracted_function == expected_func

    test_one_function(
        '_global', 'parseInt',
        lambda args: int(args[0]))

# Generated at 2022-06-14 18:33:50.380528
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    class _TestClass:
        pass
    test_class = SWFInterpreter._AVMClass(None)
    test_func = SWFInterpreter._AVMFunction(test_class, None, [], None)
    test_class.method_names.append('test_func')
    test_class.methods.append(test_func)
    interpreter = SWFInterpreter({})

    def _test_func(args):
        return args[0] + 1

    interpreter.extract_function(test_class, 'test_func', _test_func)

    instance = _TestClass()
    instance.avm_class = test_class

    assert _test_func([10]) == 11
    assert instance.test_func([10]) == 11



# Generated at 2022-06-14 18:33:59.277738
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():

    swf_dict = {}
    def extract_swf(filename):
        if filename in swf_dict:
            return swf_dict[filename]
        else:
            swf = SWFInterpreter()
            swf.load(filename)
            swf_dict[filename] = swf
            return swf

    def test_SWFInterpreter_patch_function_one(filename, method_name,
                                               expected, args):
        swf = extract_swf(filename)
        pyfunc = swf.patch_function(method_name)
        res = pyfunc(args)
        assert res == expected

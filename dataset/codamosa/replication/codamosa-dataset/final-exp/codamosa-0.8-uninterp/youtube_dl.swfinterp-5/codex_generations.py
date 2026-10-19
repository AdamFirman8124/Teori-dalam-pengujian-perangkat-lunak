

# Generated at 2022-06-14 18:26:40.165520
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    # Test method extract_class of class SWFInterpreter
    # TODO: implement it
    raise SkipTest('Not implemented')


# Generated at 2022-06-14 18:26:42.495439
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    interpreter = SWFInterpreter()
    assert isinstance(interpreter.avm1, _AVM1)



# Generated at 2022-06-14 18:26:48.440751
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = SWFInterpreter()

    swf.add_chunk('abcdefgh')
    swf.add_chunk('ijklmnop')
    swf.add_chunk('qrstuvwx')
    assert swf.read_bytes(0, 10) == b'abcdefghij'
    assert swf.read_bytes(0, 4) == b'abcd'
    assert swf.read_bytes(0, 0) == b''
    assert swf.read_bytes(5, 5) == b'fghij'
    assert swf.read_bytes(8, 2) == b'ij'
    assert swf.read_bytes(8, 4) == b'ijkl'
    assert swf.read_bytes(10, 1) == b'k'

# Generated at 2022-06-14 18:26:58.220400
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    import sys
    import io
    import unittest


# Generated at 2022-06-14 18:27:06.291797
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    # Clear previous test classes
    _builtin_classes.clear()


# Generated at 2022-06-14 18:27:18.372547
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    s = '''
        function print_string() {
            trace('string');
        }

        function trace(str) {
            return str;
        }
    '''
    s+='''
        var avm1lib;
        var loaderInfo;
        var _loader;
        var _sound;
        var _parent;
        var this;
        var _root;
        var _global;
        var _level0;
        function Frame2(){
            _root.print_string();
            _root.print_string();
            trace("hello world");
        }
    '''

    swf = SWFInterpreter(s)
    for func_name in swf.method_pyfunctions:
        f = swf.method_pyfunctions[func_name]
        f()


# Generated at 2022-06-14 18:27:26.857390
# Unit test for constructor of class SWFInterpreter

# Generated at 2022-06-14 18:27:33.999003
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from ytdl.SWFInterpreter import SWFInterpreter
    swf_file = open('testfile.swf', 'rb')
    interpreter = SWFInterpreter(swf_file)

    # Test constructor
    assert isinstance(interpreter, SWFInterpreter)

    # Assert variable in SWF file
    '''
    TODO: implement assert variable in SWF file
    '''



# Generated at 2022-06-14 18:27:43.162913
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    class DummySWFFile(object):
        def __init__(self, swf_code):
            self.swf_code = swf_code
        def read(self, *args, **kwargs):
            return self.swf_code
    def open_file(filename, *args, **kwargs):
        return DummySWFFile(swf_code)

    def absolutize(url, base_url):
        return url

    with compat_urllib_request.urlopen(
        'https://raw.github.com/rg3/youtube-dl/master/youtube_dl/utils.py'
    ) as utils_py:
        utils_code = utils_py.read()

    def parse_qs(qs):
        return compat_parse_qs(qs)

    swf_code

# Generated at 2022-06-14 18:27:54.787396
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = SWFInterpreter()
    swf.load(test_data_dir+'SWFInterpreter.swf')

    swf.get_file_version() == 9.0     # version
    # test for extracting an external class (class == "playrtmp")
    class_name = 'playrtmp'
    test_methods = ['play', 'init', 'get_video_tags']
    avm_class = swf.get_class(class_name)
    for method in test_methods:
        assert method in avm_class.method_names

    # test for extracting an internal class (class == "NetConnection")
    class_name = 'NetConnection'
    test_methods = ['call', 'connect']
    avm_class = swf.get_class(class_name)
   

# Generated at 2022-06-14 18:28:55.090257
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swfinterp = SWFInterpreter(test_swf_file('00262-rtmpe.swf'))

# Generated at 2022-06-14 18:29:03.939707
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    if not hasattr(os, 'getcwdu'):
        os.getcwdu = os.getcwd
    res = SWFInterpreter.extract_class(
        os.path.join(os.getcwdu(), 'swfinterpreter.swf'),
        '_Bootstrap', 'Bootstrap')
    assert isinstance(res, _AVMClass)
    assert res.variables.get('userAgent') == _SWFInterpreter_userAgent
    assert res.variables.get('Array') == ArrayClass
    assert isinstance(res.variables.get('String'), _AVMClass)
    assert res.variables.get('String').static_properties.get('String') == StringClass
    assert isinstance(res.static_properties.get('__init__'), types.FunctionType)
   

# Generated at 2022-06-14 18:29:11.214109
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    class TestSWF:
        def __init__(self):
            self.constant_int = []
            self.constant_uint = []
            self.constant_double = []
            self.constant_strings = []
            self.constant_namespaces = []
            self.constant_namespace_sets = []
            self.constant_multinames = []

    swf = TestSWF()

    swf.constant_multinames.append(
        _Multiname(kind=0x07, index=0, namespaces=[0], index2=0))
    swf.constant_namespaces.append(_Namespace(kind=0x16, name='as3'))
    swf.constant_namespace_sets.append([0])

# Generated at 2022-06-14 18:29:19.776540
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swfdata = open(os.path.join(os.path.dirname(__file__),
                                    'test-audio.swf'), 'rb').read()
    interpreter = SWFInterpreter(swfdata)
    assert interpreter.swf is not None
    assert interpreter.swf.version == 13
    assert interpreter.swf.tags[0].code == SWF.DEFINESPRITE
    assert isinstance(interpreter.swf.tags[0], TagDefineSprite)
    sprite_tag = interpreter.swf.tags[0]
    assert isinstance(sprite_tag.tags[0], TagDoAction)
    action_tag = sprite_tag.tags[0]
    assert isinstance(action_tag.actions, list)
    assert isinstance(action_tag.actions[0], ActionPush)

# Generated at 2022-06-14 18:29:27.415786
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interpreter = SWFInterpreter()
    # TODO: implement
    # Test with a function from a source file
    source_file = '../swfdecompyler/swfobjects/8.swf'
    interpreter.decompile(source_file)
    avm_class = interpreter.classes['_level0']
    avm_class.extract_methods()
    func = avm_class.method_pyfunctions['func']
    res = func([])

    # Test that the result is as expected
    # TODO: implement

# Generated at 2022-06-14 18:29:36.949525
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    class DecodingError(Exception):
        pass
    # Class that wraps a BytesIO and raises an exception if a string is not
    # fully consumed
    class StrictBytesIO(BytesIO):
        def read(self, n):
            res = super(StrictBytesIO, self).read(n)
            if len(res) != n:
                raise DecodingError(
                    'Could not read %d bytes, got %d' % (n, len(res)))
            return res

    def test_u8(value, expected):
        avm_interp = SWFInterpreter()
        avm_interp._avm_swf = StrictBytesIO(compat_chr(value))
        res = avm_interp.u8()

# Generated at 2022-06-14 18:29:38.017330
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    assert True, 'Not implemented'

# Generated at 2022-06-14 18:29:46.500246
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swfi = SWFInterpreter()
    swfi.load(os.path.join(
        os.path.dirname(__file__), 'testdata/swf/test_extract_class.swf'))
    res = swfi.extract_class()
    assert 'frame1' in res.static_properties
    assert isinstance(res.static_properties['frame1'], list)
    assert len(res.static_properties['frame1']) == 4
    assert 'onRelease' in res.static_properties
    assert callable(res.static_properties['onRelease'])
    assert 'stop' in res.static_properties
    assert callable(res.static_properties['stop'])
    assert 'trace' in res.static_properties
    assert callable(res.static_properties['trace'])




# Generated at 2022-06-14 18:29:56.588296
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:30:07.777599
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from .parser import SWFParser, SWFInterpreter, SWFTag
    import struct
    import os

    def tag_17(data, pos):
        return SWFTag(17, data, pos)

    def read_rect(data, pos):
        flags_byte = ord(data[0])
        end_pos = 1
        if flags_byte & 0xff & (0x80 >> 0):
            end_pos += 3
        if flags_byte & 0xff & (0x80 >> 1):
            end_pos += 3
        if flags_byte & 0xff & (0x80 >> 2):
            end_pos += 3
        if flags_byte & 0xff & (0x80 >> 3):
            end_pos += 3

# Generated at 2022-06-14 18:32:02.433441
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf = SWFInterpreter(open(os.path.join(_TEST_DIR, 'flash.swf'), 'rb'))

# Generated at 2022-06-14 18:32:10.315957
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    inter = intepreter_class()
    assert len(inter.constant_strings) == 14
    assert inter.constant_strings[0] == ''
    assert inter.constant_strings[1] == 'flash.net::NetStreamPlayTransitions'
    assert inter.constant_strings[2] == 'code'
    assert inter.constant_strings[3] == 'description'
    assert inter.constant_strings[4] == 'details'
    assert inter.constant_strings[5] == 'level'
    assert inter.constant_strings[6] == ''
    assert inter.constant_strings[7] == 'NetStream.Play.StreamNotFound'
    assert inter.constant_strings[8] == 'Stream not found: '

# Generated at 2022-06-14 18:32:13.307731
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    """Test for constructor of class SWFInterpreter."""
    swf = SWFInterpreter()
    assert isinstance(swf, SWFInterpreter)

# Generated at 2022-06-14 18:32:19.806428
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    data = b'\x43\x57\x53\x12\x07\x00\x00\x00'
    coder = BytesIO(data)

    swf = io.BufferedIOBase()
    swf.swf = SWF(coder)
    swf.frames = []

    interp = SWFInterpreter(swf)

    # Testing get_avm_class('')
    assert interp.get_avm_class('').name == 'Class'
    assert interp.get_avm_class('undefined').name == 'undefined'
    assert interp.get_avm_class('Object').name == 'Object'
    assert interp.get_avm_class('String').name == 'String'

# Generated at 2022-06-14 18:32:24.849249
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    """Test method patch_function of class SWFInterpreter"""
    swf = SWFInterpreter('tests/test.swf')
    def _patched_setTimeout(self, *args):
        return self.__old_setTimeout(*args) + 1

    swf.patch_function('flash.utils::setTimeout', _patched_setTimeout)
    assert swf.evaluate() == 6


# Generic unit test for class SWFInterpreter

# Generated at 2022-06-14 18:32:35.809979
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:32:44.470447
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from collections import namedtuple

    def _do_test(code, expected_result):
        swf = SWFInterpreter()
        swf.code = code
        func = swf.patch_function()
        result = func()
        assert isinstance(result, expected_result), repr(result)

    # swf_0.py

# Generated at 2022-06-14 18:32:57.052475
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    swf = SWFInterpreter()
    swf.parse(
        pkg_resources.resource_stream(
            __name__, 'data/test/playerProductInstall.swf'))

# Generated at 2022-06-14 18:33:09.266899
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from .bitstream import BitStream
    from .utils_swf import swf_parse_tag

    # SWF header

# Generated at 2022-06-14 18:33:19.882490
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from .swf_utils import read_abcdump

    def test_func(interpreter):
        avm_file = open(os.path.join(
            os.path.dirname(__file__), 'tests', 'abc',
            interpreter.abc_file_name + '.abc'), 'rb')
        abcdump = read_abcdump(avm_file, raw=True)

        interpreter.method_names = [x.split()[-1]
                                    for x in abcdump.splitlines()
                                    if 'trait Method' in x]

        interpreter.extract_function('Main', 'public$main')

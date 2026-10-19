

# Generated at 2022-06-14 18:25:08.694890
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    path = os.path.join(os.path.dirname(__file__), 'tests', 'swf', 'test1.swf')
    swf = SWFInterpreter(open(path, 'rb'))
    swf.extract_function(swf.classes['test1.Test'], 'test_str')

    path = os.path.join(os.path.dirname(__file__), 'tests', 'swf', 'test2.swf')
    swf = SWFInterpreter(open(path, 'rb'))
    swf.extract_function(swf.classes['test2.Test'], 'test_extract_url')
    swf.extract_function(swf.classes['test2.Test'], 'test_custom_headers')
    swf.extract_function

# Generated at 2022-06-14 18:25:13.286379
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    data = io.BytesIO(compat_urllib_request.urlopen(
        'https://raw.githubusercontent.com/rg3/youtube-dl/master/youtube_dl/extractor/crunchyroll.py').read())
    # This is not very useful; it's just to prevent Pyflakes warnings
    return SWFInterpreter(data)



# Generated at 2022-06-14 18:25:16.968744
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    fileobj = io.BytesIO(SWF_INTERPRETER_TEST_FILE)
    interpreter = SWFInterpreter(fileobj)
    assert isinstance(interpreter, SWFInterpreter)


# Generated at 2022-06-14 18:25:24.619795
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    import unittest
    import io

    from .swfcodec import BitReader, read_u16, read_u8

    class _FakeClass(object):
        variables = {}
        method_names = set()

    class TestCase(unittest.TestCase):

        def setUp(self):
            self.interp = SWFInterpreter()

        def _read_code(self, buf):
            reader = BitReader(io.BufferedReader(io.BytesIO(buf)))
            code_length = read_u16(reader)
            return reader.read_bytes(code_length)

        def _read_opcode(self, reader):
            opcode = read_u8(reader)
            if opcode == 0x96:  # getlex
                return self._read_getlex_opcode(reader)


# Generated at 2022-06-14 18:25:35.990351
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    import io
    import unittest


# Generated at 2022-06-14 18:25:44.335229
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'test',
        'test_SWFInterpreter_extract_class.swf')
    i = SWFInterpreter()
    i.read_swf(filename)
    class_name = 'test.test_SWFInterpreter_extract_class'
    res = i.extract_class(class_name)
    assert res.variables['a'] == 100
    assert res.variables['b'] == 200
    assert res.static_properties['f']() == 300
    assert res.static_properties['g']() == 400
    assert res.static_properties['h'] == 'static'
    assert res.static_properties['i'] == 'static private'
    tovar = i

# Generated at 2022-06-14 18:25:46.541762
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    a = SWFInterpreter()



# This class helps parse a SWF file.

# Generated at 2022-06-14 18:25:54.323796
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf_data = b'\x46\x57\x53\x09\x00\x3f\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03'
    with open('tmp.swf', 'wb') as out:
        out.write(swf_data)
    swf = SWFInterpreter('tmp.swf')
    swf.extract_class('root0', 'TestClass', 'TestClass.as')

# Generated at 2022-06-14 18:26:00.943134
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    s = SWFInterpreter(compat_urllib_request.urlopen(
        'https://github.com/rg3/youtube-dl/raw/master/test/swfinterpreter/' +
        'test_class.swf').read())
    TestClass = s.extract_class('TestClass')
    assert TestClass is not None
    assert TestClass.static_properties['testStr'] == 'bar'
    assert TestClass.static_properties['testNum'] == 42
    assert TestClass.static_properties['testBool'] == False
    obj = TestClass.make_object()
    assert obj.properties['testProp'] == 'foo'


# Generated at 2022-06-14 18:26:11.775555
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from io import BytesIO as IO
    coder = SWFInterpreter.make_coder(IO(b''), 0)

    def _read_byte(coder):
        return ord(coder.read(1))

    def u8(coder):
        return _read_byte(coder)

    def s24(coder):
        return struct.unpack('<l', b'\x00' + coder.read(3))[0]

    def s_u30(coder):
        res = 0
        shift = 0
        while True:
            byte = _read_byte(coder)
            res |= (byte & 0x7F) << shift
            if byte & 0x80 == 0:
                break
            shift += 7
        if res & 0x10000000:
            res -= 0

# Generated at 2022-06-14 18:27:21.693000
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:27:32.361925
# Unit test for constructor of class SWFInterpreter

# Generated at 2022-06-14 18:27:38.631620
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():

    class _FakeSWF(object):
        def __init__(self, path):
            self.f = open(path, 'rb')
        def read_data_type(self, dt):
            if dt == 'SI32':
                return struct.unpack('>i', self.f.read(4))[0]
            elif dt == 'UI8':
                return struct.unpack('B', self.f.read(1))[0]
            elif dt == 'UI16':
                return struct.unpack('>H', self.f.read(2))[0]
            elif dt == 'UI32':
                return struct.unpack('>I', self.f.read(4))[0]

# Generated at 2022-06-14 18:27:45.132236
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    swf = _get_test_file(SAMPLE_VIDEO_SWF)
    swf_interpreter = SWFInterpreter(swf)
    player = swf_interpreter.get_class('Player')
    player.methods[0]
    func = swf_interpreter.extract_function(player, 'init')
    assert func([], []) is None


# Generated at 2022-06-14 18:27:56.288871
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    import os
    import tempfile
    from .swfparser import SWFParser

    fd, filename = tempfile.mkstemp(suffix='.swf', prefix='pyavm2_')
    os.write(fd, _SWF_INTERPRETER_TEST)
    os.close(fd)

    swf = SWFParser(filename, verbose=False)
    for tag in swf.iter_all_tag():
        if tag.code == 82:
            break
    else:
        raise ValueError('No ABC tag found in test SWF file')

    abc = tag.body

    interpreter = SWFInterpreter(abc.ABCFile)
    interpreter.extract_function('TestClass', 'testMethod')


# Generated at 2022-06-14 18:28:07.658616
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    avm = SWFInterpreter('test_media/test.swf')
    assert avm.version == 9
    assert avm.movie_width == 320
    assert avm.movie_height == 240
    assert avm.frame_rate == 30.0
    assert avm.frame_count == 1
    assert avm.script_counter == 3
    assert avm.main_class == 'MainTimeline'

    assert len(avm.classes) == 14

# Generated at 2022-06-14 18:28:18.360044
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    from .bitstring import ConstBitStream

    def test_read_u16(data, expected):
        cbs = ConstBitStream(data)
        res = read_u16(cbs)
        assert res == expected
        assert cbs.read(16).uint == 0

    def test_read_u30(data, expected):
        cbs = ConstBitStream(data)
        res = read_u30(cbs)
        assert res == expected
        assert cbs.read(16).uint == 0

    def test_read_u32(data, expected):
        cbs = ConstBitStream(data)
        res = read_u32(cbs)
        assert res == expected
        assert cbs.read(16).uint == 0


# Generated at 2022-06-14 18:28:30.939190
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:28:38.833305
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():

    # Read the ABC file
    f = open(os.path.join(os.path.dirname(__file__), 'tests/method.abc'), 'rb')
    abc_data = f.read()
    f.close()
    
    # Extract the method body
    swf_interpreter = SWFInterpreter(abc_data)
    method_body = swf_interpreter.method_bodies[0]
    avm_class = swf_interpreter.find_class(method_body.method.abc_class.name)
    
    # Extract the function
    function = swf_interpreter.extract_function(avm_class, method_body.method.name)
    
    # Test
    args = [0, 'test']

# Generated at 2022-06-14 18:28:49.588984
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    interp = SWFInterpreter()

# Generated at 2022-06-14 18:30:48.290915
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    from io import BytesIO
    class SWF(object):
        def __init__(self, data):
            self.data = data
    interpreter = SWFInterpreter()
    interpreter.logger = compat_str
    interpreter.log_print = print

# Generated at 2022-06-14 18:30:54.356976
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    avm_class = SWFInterpreter(open(os.path.join(
        os.path.dirname(__file__), 'swf/test_object.swf'), 'rb').read())

    assert avm_class.instance_variable_names == []
    assert avm_class.static_variable_names == ['testvar']
    assert avm_class.method_names == ['testmethod']

    test_method = avm_class.extract_method('testmethod')
    assert test_method

    assert sorted(avm_class.static_properties.keys()) == ['testvar']

    obj = avm_class.make_object()
    assert obj.avm_class is avm_class
    assert obj == {'testvar': None, 'testmethod': test_method}
test_SWFInterpreter

# Generated at 2022-06-14 18:31:05.817263
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    # .swf files are located in common directory
    TEST_FILES_DIR = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'common', 'test')

    for swf_file in os.listdir(TEST_FILES_DIR):
        if not swf_file.endswith('.swf') or '-broken' in swf_file:
            continue
        # Extract all classes from file
        with open(os.path.join(TEST_FILES_DIR, swf_file), 'rb') as inf:
            swf_interpreter = SWFInterpreter(inf)
            all_names = swf_interpreter.get_all_names()
            for class_name in all_names:
                _, avm_

# Generated at 2022-06-14 18:31:13.734727
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interpreter = SWFInterpreter(open('data/sample1.swf', 'rb'))
    interpreter.extract_function(interpreter.top_class, 'get_chapters')
    interpreter.extract_function(interpreter.top_class, 'get_chapter_info')
    interpreter.extract_function(interpreter.top_class, 'get_video_url_1')
    interpreter.extract_function(interpreter.top_class, 'get_video_url')
    interpreter.extract_function(interpreter.top_class, 'get_video_map')
    interpreter.extract_function(interpreter.top_class, 'get_video_info_1')
    interpreter.extract_function(interpreter.top_class, 'get_video_info')
    interpreter.ext

# Generated at 2022-06-14 18:31:17.134200
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf_file = open(
        path.join(path.dirname(path.abspath(__file__)), 'youtube.swf'), 'rb')
    SWFInterpreter(swf_file)
    swf_file.close()


# Generated at 2022-06-14 18:31:26.551909
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():

    def printobj(s):
        print(s.encode('utf-8'))


# Generated at 2022-06-14 18:31:36.884428
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:31:48.706807
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from collections import namedtuple
    from io import BytesIO
    from srsly.pickle import pickle, Unpickler

    ConstantPoolInfo = namedtuple(
        'ConstantPoolInfo', ['strings', 'namespaces'])
    MethodInfo = namedtuple(
        'MethodInfo', ['code'])
    MethodBody = namedtuple(
        'MethodBody', ['max_stack', 'local_count', 'init_scope_depth',
                       'max_scope_depth', 'code'])

    interpreter = SWFInterpreter()

    # See tests/test_extract.py, test_extract_xml_field

# Generated at 2022-06-14 18:31:59.712199
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    sei = _SWFExtractInfo()

    with open(os.path.join(os.path.dirname(__file__), 'swf', 'swfinterpreter.swf'), 'rb') as swf_file:
        swf_interpreter_bytes = swf_file.read()
    sei.read_swf(swf_interpreter_bytes)

    assert len(sei.avm1classes) == 1
    avm_class = sei.avm1classes[0]
    assert avm_class.class_name == '_level0'

    interpreter = SWFInterpreter(sei.avm1classes)
    interpreter.patch_function(avm_class, 'doSomething', (lambda test: test * 2))


# Generated at 2022-06-14 18:32:07.716674
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    class SWFSpec(object):
        pass
    swf = SWFSpec()
    swf.file = io.BytesIO(open(
        os.path.join(os.path.dirname(__file__), 'tests', 'test.swf'),
        'rb').read())
    swf.screensize = (800, 600)
    swf.framecount = 5
    swf._version = 5


# Generated at 2022-06-14 18:25:17.298189
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf = open(os.path.join(data_dir, 'swf/test.swf'), 'rb').read()
    interpreter = SWFInterpreter(swf)
    interpreter.extract_class('TestClass')



# Generated at 2022-06-14 18:25:21.631398
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    # test loading a file
    with io.open(os.path.join(os.path.dirname(__file__), 'simple.swf'), 'rb') as f:
        swf = SWFInterpreter(f)
        assert swf.version == 10
        assert swf.file_length == 914


# Useful functions for SWF


# Generated at 2022-06-14 18:25:23.389043
# Unit test for method __repr__ of class _ScopeDict
def test__ScopeDict___repr__():
    assert _ScopeDict(None).__repr__() == 'None__Scope({})'

# Generated at 2022-06-14 18:25:33.911671
# Unit test for method __repr__ of class _ScopeDict
def test__ScopeDict___repr__():
    from .pytest_utils import random_test_class_name
    class MockAVMClass:
        def __init__(self):
            self.name = random_test_class_name()
        def __repr__(self):
            return 'MockAVMClass<%s>' % self.name
    mock_avm_class = MockAVMClass()
    scope = _ScopeDict(mock_avm_class)
    scope['abc'] = 123
    scope['def'] = 456
    assert (
        repr(scope) ==
        'MockAVMClass<%s>__Scope({"def": 456, "abc": 123})'
        % mock_avm_class.name)
test__ScopeDict___repr__()



# Generated at 2022-06-14 18:25:41.632441
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    import zlib
    # This is a dummy file, with a compressed SWF that contains a single
    # function (the name is "e", and it will return a number 42)
    with open('pytube/swfinterpreter_test1.swf', 'rb') as f:
        swf_data = f.read()
    data = zlib.decompress(swf_data)
    interpreter = SWFInterpreter(data)
    interpreter.patch_function('e')
    assert interpreter.avm_class.method_pyfunctions['e'] == 42



# Generated at 2022-06-14 18:25:54.361574
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    def assert_equal(a, b):
        if a != b:
            print(a, b)
            raise AssertionError

    flash_ver = 0x10
    code = b'\x12\x00\x00\x00'  # pushbyte
    code += b'\x0B\x00\x00\x00'  # pushbyte
    code += b'\x47'  # returnvoid
    coder = io.BytesIO(b'\x00\x00\x00\x00' + code)
    coder.seek(4)
    swf_interpreter = SWFInterpreter(flash_ver)
    swf_interpreter.patch_function(coder, code)
    assert_equal(len(swf_interpreter.constant_strings), 0)


# Generated at 2022-06-14 18:26:00.970112
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interpreters = []
    for _ in range(10):
        _, parser = parse_swf('../tests/swf/moviestar-v6.swf')
        cls = parser.swf.tags[7].body
        intp = SWFInterpreter(parser.swf)
        intp.load_class(cls)
        interpreters.append(intp)

    intp = interpreters.pop()
    cls = intp.avm_classes['com.longtailvideo.jwplayer.media::MediaProvider']
    assert cls.method_pyfunctions['__init__'].__name__ == '__init__'
    assert cls.method_pyfunctions['__init__'].__code__.co_argcount == 3

# Generated at 2022-06-14 18:26:11.816993
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    swf = SWFInterpreter('tests/swf_interp_test_A.swf')

    reference_point = swf.avm_class_dict['A'].find_trait('p')
    assert reference_point['x'] == 10
    assert reference_point['y'] == 20
    assert reference_point['w'] == 0.5
    assert reference_point['h'] == 1
    assert reference_point['color'] == 'black'
    assert reference_point['style'] == 'cross'

    reference_rectangle = swf.avm_class_dict['A'].find_trait('r')
    assert reference_rectangle['x'] == 10
    assert reference_rectangle['y'] == 20
    assert reference_rectangle['w'] == 30
    assert reference_rectangle['h'] == 40


# Generated at 2022-06-14 18:26:20.982470
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf_interpreter = SWFInterpreter(None, None)
    swf_interpreter.abc_index = 0
    abc_tags = {
        0x03: 'ABC',
        0x52: 'DoABC2',
    }
    swf_interpreter.abc_tags = abc_tags
    swf_interpreter.method_names = {
        0: 'add',
    }
    swf_interpreter.method_bodies = {
        0: 'add body',
    }

# Generated at 2022-06-14 18:26:25.461061
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    with open(os.path.join(common.RSRC_DIR, 'bw.swf'), 'rb') as f:
        swf = SWFInterpreter(f.read())
    for avm_class in swf.avm_classes.values():
        for mname in avm_class.method_names:
            resfunc = swf.extract_function(avm_class, mname)
            assert resfunc


# Interpreter for a SWF file

# Generated at 2022-06-14 18:27:27.596846
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    from . import _swf_interpreter_data as _data

    swf_interpreter = SWFInterpreter(_data.swf_data)
    swf_interpreter.extract_class('net.i2p.i2ptunnel.udp.UDPEndpoint')
    udp_endpoint_class = swf_interpreter.classes['net.i2p.i2ptunnel.udp.UDPEndpoint']
    assert udp_endpoint_class.static_properties['$id'] == 'net.i2p.i2ptunnel.udp.UDPEndpoint'
    assert udp_endpoint_class.static_properties['$isInterface'] is False
    assert udp_endpoint_class.static_properties['_dataMap'] is None
    assert udp_

# Generated at 2022-06-14 18:27:31.240408
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf = SWFInterpreter(None)
    constants = []
    swf.extract_class(0, constants)



# Generated at 2022-06-14 18:27:41.068407
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    from io import BytesIO
    from .abc import read_abc_file
    from .abc import build_script_class


# Generated at 2022-06-14 18:27:52.852623
# Unit test for method patch_function of class SWFInterpreter

# Generated at 2022-06-14 18:27:55.195103
# Unit test for method __repr__ of class _ScopeDict
def test__ScopeDict___repr__():
    assert repr(_ScopeDict(_AVMClass_Object(_AVMClass_Object('Test')))) == "Test__Scope({'__proto__': {}},)"
test__ScopeDict___repr__()

# Generated at 2022-06-14 18:28:07.224574
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    for i in range(1):
        swf = SWF()
        swf.parse(open(os.path.join(os.path.dirname(__file__),
                                    'swf/test_as3_%d.swf' % i), 'rb').read())
        avm_classes = {}
        for name, avm_class in sorted(swf.avm_classes.items()):
            assert name not in avm_classes
            avm_classes[name] = avm_class
        for name in sorted(swf.avm_classes.keys()):
            try:
                swf.extract_function(avm_classes[name], 'Main')
            except Exception:
                print(name)
                raise


# Generated at 2022-06-14 18:28:18.008806
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    """Unit test for method extract_class of class SWFInterpreter"""
    # Test all classes
    for tag_id in (39, 71, 87):
        raw_data = open(
            os.path.join(TEST_DATA_DIR, 'test%d.swf' % tag_id), 'rb').read()
        swf = SWFInterpreter(raw_data)
        swf.extract_tag(tag_id)
    # Test specific classes
    def test_class(tag_id, class_idx):
        """Test a specific class"""
        raw_data = open(
            os.path.join(TEST_DATA_DIR, 'test%d.swf' % tag_id), 'rb').read()
        swf = SWFInterpreter(raw_data)
        swf.ext

# Generated at 2022-06-14 18:28:23.679819
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():

    swf = open(os.path.join(SWF_TEST_DIR, 'test.swf'), 'rb').read()
    swfobj = SWF(swf)
    script = swfobj.atoms[-1]
    interpreter = SWFInterpreter(script)
    interpreter.extract_function(script, 'getSwfVars', args=[])
    assert interpreter.extract_function(script, 'encode', args=['test']) == 'dGVzdA=='

# Generated at 2022-06-14 18:28:24.982211
# Unit test for method __repr__ of class _ScopeDict
def test__ScopeDict___repr__():
    obj = _ScopeDict(object())
    assert repr(obj) == ('%s__Scope({})' % obj.avm_class.__name__), repr(obj)



# Generated at 2022-06-14 18:28:29.752363
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    interpreter = SWFInterpreter()
    assert interpreter.multinames[0] == 'empty'
    assert interpreter.multinames[1] == 'container'
    assert interpreter.multinames[2] == 'flash.display'
    assert interpreter.multinames[3] == 'flash.events'
    assert interpreter.multinames[4] == 'flash.system'
    assert interpreter.multinames[5] == 'flash.utils'
    assert interpreter.multinames[6] == 'trace'

    assert interpreter.constant_strings[0] == 'Class %r not found in file %r'
    assert interpreter.constant_strings[1] == 'NetConnection'
    assert interpreter.constant_strings[2] == 'NetStream'
    assert interpreter.constant_strings[3] == 'Stream'

# Generated at 2022-06-14 18:30:01.261588
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    import unittest
    import io
    import os

    class TestInterpreter(unittest.TestCase):
        def test_basic_input_output(self):
            with open(os.path.join(os.path.dirname(__file__),
                                   'basic_tests.txt'), 'rb') as f:
                for line in f:
                    if not line or line.startswith(b'#'):
                        continue
                    cmd, data = line.strip().split(' ', 1)
                    if cmd == b'input':
                        avm = SWFInterpreter(io.BytesIO(data))

# Generated at 2022-06-14 18:30:09.898253
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    with open(path.join(
        path.dirname(path.abspath(__file__)), '../tests/test1.swf'), 'rb') as f:
        swf = f.read()
    swf = swf[8:]  # Skip header
    tag = Tag.parse(swf)
    s = SWFInterpreter(tag)

    # Create a decompiler for the "main" method
    d = DummyASM()
    d.initialize1(s.avm_class, 'main', s.methods[s.avm_class.method_names.index('main')])
    d.initialize2()

# Generated at 2022-06-14 18:30:20.450805
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    swf = SWFInterpreter()
    swf.constant_strings = [
        None,
        'String',
        'undefined',
        'Number',
        '+',
    ]

    # str_0_unnamed_0 = 'String';
    # str_1_unnamed_0 = 'undefined';
    # str_2_unnamed_0 = 'Number';
    # str_3_unnamed_0 = '+';

# Generated at 2022-06-14 18:30:32.647691
# Unit test for method extract_function of class SWFInterpreter

# Generated at 2022-06-14 18:30:37.906949
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    interpreter = SWFInterpreter('testdata/input_1.swf')
    class_1 = interpreter.classes['com.adobe.Flashgateway.ObjectEncoder']
    callable_1 = class_1.method_pyfunctions['getExternalInterface']
    assert callable_1.__name__ == 'getExternalInterface'


# Generated at 2022-06-14 18:30:48.473007
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    interpreter = _SWFInterpreter()
    interpreter.strings = [
        'TestClass', 'method', 'arg',
        'static_var', 'arg', 'static_method',
    ]
    interpreter.constant_strings = [
        'TestClass', 'static_var', 'static_method',
    ]
    interpreter.multinames = [
        'TestClass', 'static_var', 'static_method', 'method',
    ]


# Generated at 2022-06-14 18:30:58.836694
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    # Test imports
    import binascii
    import os
    import random
    import shutil
    import tempfile
    import unittest
    import zlib

    # Test the helper function that generates random bytes
    def randbytes(n):
        return b''.join([
            compat_struct_pack(b'B', random.randrange(256))
            for _ in range(n)])

    def nop(abc):
        pass

    def _get_swf_tags(tags):
        from .swfdecompiler import get_swf_tags

        return get_swf_tags(io.BytesIO(binascii.a2b_hex(tags)))

    class SWFInterpreterTest(unittest.TestCase):
        def test_simple(self):
            abc_data = _get_

# Generated at 2022-06-14 18:31:09.840901
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    import os
    import os.path
    import tempfile
    import shutil

    def _test_SWFInterpreter_fnc(stream, swf_version):
        # Create temporary folder for unit test
        fd, path = tempfile.mkstemp()
        os.close(fd)
        tmp_dir = path + '.tmp'
        os.mkdir(tmp_dir)

# Generated at 2022-06-14 18:31:15.716768
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = SWFInterpreter(io.BytesIO())
    assert swf.file_header['Signature'] == b'FWS'
    assert swf.file_header['FrameSize'] == (0, 0, 0, 0)
    assert swf.file_header['FrameRate'] == 0
    assert swf.file_header['FrameCount'] == 0



# Generated at 2022-06-14 18:31:19.465619
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    swf = open_swf('testsuite/swf/AMF3/AMF3.swf')
    swf.show_info()
    swf.extract_class('Dashboard')



# Generated at 2022-06-14 18:33:15.892079
# Unit test for method patch_function of class SWFInterpreter
def test_SWFInterpreter_patch_function():
    import os
    import sys
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    # Create instance

# Generated at 2022-06-14 18:33:23.019507
# Unit test for method extract_function of class SWFInterpreter
def test_SWFInterpreter_extract_function():
    class _TestSWFInterpreter(SWFInterpreter):
        def __init__(self, constant_strings=None, multinames=None,
                     strings=None, script=None, version=None):
            assert constant_strings is not None
            assert multinames is not None
            assert strings is not None
            assert script is not None
            assert version is not None
            self.constant_strings = constant_strings
            self.multinames = multinames
            self.strings = strings
            self.script = script
            self.version = version


# Generated at 2022-06-14 18:33:28.690740
# Unit test for method extract_class of class SWFInterpreter
def test_SWFInterpreter_extract_class():
    open_swf = os.path.join(os.path.split(__file__)[0], 'swf/test1.swf')
    swf = open(open_swf, 'rb').read()
    handler = SWFInterpreter(swf)
    handler.extract_class('_level0')
    assert isinstance(handler.classes['_level0'], _AVMClass)


# Generated at 2022-06-14 18:33:40.549975
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    fname = 'getid3/TEST.swf'
    with open(fname, 'rb') as f:
        swf = SWF(f)
        assert swf.header.signature[0] == ord('C')
        assert swf.header.signature[1] == ord('W')
        assert swf.header.signature[2] == ord('S')
        assert swf.header.version == 9
        assert swf.header.file_length == 538
        assert swf.tags == [SWFTag(12, b'\x02\x00\x01\x00\x02\x00\x01\x00\x00\x00\x00\x00')]

# Generated at 2022-06-14 18:33:49.854222
# Unit test for constructor of class SWFInterpreter

# Generated at 2022-06-14 18:33:54.678455
# Unit test for constructor of class SWFInterpreter
def test_SWFInterpreter():
    swf = open(os.path.join(os.path.dirname(__file__), 'input', 'test.swf'), 'rb').read()
    avm = SWFInterpreter(swf)
    assert avm.version == 9
    assert avm.constant_strings[1] == 'onLoad'
    assert avm.class_name_from_id(1) == 'Object'
    assert avm.class_name_from_id(2) == 'Function'
    assert avm.classes[1].name == 'Object'
    assert avm.classes[2].name == 'Function'
    assert isinstance(avm.classes[1], _AVMClass)
    assert isinstance(avm.classes[2], _AVMClass)